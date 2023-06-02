import os
import pickle
import numpy as np


class QTable:
    def __init__(self, path, num_available_actions: int = None) -> None:
        self.table = {}
        if path is not None and os.path.exists(path):
            with open(path, 'rb') as fp:
                self.table = pickle.load(fp).table
                print("Table loaded!")
            
        self.num_available_actions = num_available_actions

    def mine(self, state):
        if state in self.table.keys():
            action = np.argmax(self.table[state])
            return action
        return None

    def get_score(self, state, action):
        if state in self.table.keys():
            return self.table[state][action]
        return 0

    def set_score(self, state, action, score):
        if state not in self.table.keys():
            self.table[state] = np.zeros(shape=(self.num_available_actions, ))
        self.table[state][action] = score


    def __str__(self) -> str:
        res = ""
        for state, scores in self.table.items():
            res += "\n{} | mean: {:.4f} | max: {:.4f}".format(state, np.mean(scores), np.max(scores))
        return str(res)
