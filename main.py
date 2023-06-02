import sys
sys.path.append('../')

from args import get_args
from agent import TrainingBoxer, FighterBoxer, RandomBoxer
from game import Game
from qtable import QTable
from hyperparameter import Hyperparameters

if __name__ == "__main__":
    args = get_args()

    if args.train:
        q_table = QTable(path=args.q_table)
        params = Hyperparameters(gamma=args.gamma, alpha=args.alpha, epsilon=args.epsilon)
        boxer = TrainingBoxer(q_table=q_table, params=params,resume=args.resume)
    elif args.fight:
        q_table = QTable(path=args.q_table)
        boxer = FighterBoxer(q_table=q_table)
    elif args.random:
        boxer = RandomBoxer()
    else:
        raise Exception('train or fight? use one of `--train` `--fight`')

    game = Game(boxer=boxer, start_episode=args.start_episode)
    game.start()
