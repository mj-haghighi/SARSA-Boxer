import sys
sys.path.append('../')

from args import get_args
from agent import TrainingBoxer, FighterBoxer, RandomBoxer
from game import Game

if __name__ == "__main__":
    args = get_args()

    if args.train:
        boxer = TrainingBoxer(q_table_path=args.q_table)
    elif args.fight:
        boxer = FighterBoxer(q_table_path=args.q_table)
    elif args.random:
        boxer = RandomBoxer(q_table_path=args.q_table)
    else:
        raise Exception('train or fight? use one of `--train` `--fight`')

    game = Game(boxer=boxer)
    game.start()
