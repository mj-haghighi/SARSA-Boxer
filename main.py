from .args import get_args
from .agent import Boxer


if __name__ == "__main__":
    args = get_args()
    boxer = Boxer(q_table_path=args.q_table)

    if args.train:
        boxer.train(args.resume)
    elif args.fight:
        boxer.fight()
    else:
        raise Exception('train or fight? use one of `--train` `--fight`')
