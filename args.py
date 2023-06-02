import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Would you like to train boxer or figth?')

    # Add arguments
    parser.add_argument('--train', action='store_true',help='start to train boxer')
    parser.add_argument('--resume', action='store_true',help='resume training')
    parser.add_argument('--q_table', type=str, help='path to q-table')
    parser.add_argument('--fight', action='store_true', help='start to fight!')
    parser.add_argument('--random', action='store_true', help='start to act randomly!')
    parser.add_argument('--gamma', type=float, default=0.9, help='gamma | hyper parameter')
    parser.add_argument('--alpha', type=float, default=0.8, help='learning rate')
    parser.add_argument('--epsilon', type=float, default=1.0, help='epsilon gready')
    parser.add_argument('--start_episode', type=int, help='start from episode "start_episode", use when resuming training process')

    # Parse the arguments
    args = parser.parse_args()

    return args
