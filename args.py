import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Would you like to train boxer or figth?')

    # Add arguments
    parser.add_argument('--train', action='store_true',help='start to train boxer')
    parser.add_argument('--resume', action='store_true',help='resume training')
    parser.add_argument('--q_table', type=str, help='path to q-table')
    parser.add_argument('--fight', action='store_true', help='start to fight!')
    parser.add_argument('--random', action='store_true', help='start to act randomly!')

    # Parse the arguments
    args = parser.parse_args()

    return args
