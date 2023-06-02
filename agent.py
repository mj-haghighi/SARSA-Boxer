import os
import pickle
import numpy as np
from qtable import QTable
from img_utils import find_heads, encode_state
from hyperparameter import Hyperparameters


class Boxer:
    """
    Boxer agnet class
    """

    def __init__(self, q_table: QTable = None, params: Hyperparameters = None) -> None:
        self.__action_space = None
        self.q_table = q_table
        self.params = params

    @property
    def action_space(self):
        return self.__action_space

    @action_space.setter
    def action_space(self, value):
        self.__action_space = value
        self.q_table.num_available_actions = value.n

    def take_action(self, observation, reward):
        raise Exception("This method os not imlemented")


class RandomBoxer(Boxer):
    def __init__(self) -> None:
        super().__init__(None, None)

    def take_action(self, observation, reward):
        return self.action_space.sample()


class TrainingBoxer(Boxer):
    def __init__(self, q_table: QTable = None, params: Hyperparameters = None, resume: bool = False) -> None:
        super().__init__(q_table, params)
        self.resume = resume
        self.state = None
        self.action = None

    def update(self, new_state, new_action, reward):
        """
        Function to learn the Q-value
        """
        predict = self.q_table.get_score(self.state, self.action)
        target = reward + self.params.gamma.value *\
            self.q_table.get_score(new_state, new_action)
        score = predict + self.params.alpha.value * (target - predict)
        self.q_table.set_score(self.state, self.action, score)

    def take_action(self, observation, reward):
        boxer, enemy = find_heads(image=observation)
        new_state = encode_state(boxer, enemy)
        new_action = None
        if np.random.uniform(0, 1) > self.params.epsilon.value:
            new_action = self.q_table.mine(new_state)
        if new_action is None:
            new_action = self.action_space.sample()

        if self.state is not None:
            self.update(new_state, new_action, reward)

        self.action = new_action
        self.state = new_state

        return new_action


class FighterBoxer(Boxer):
    pass
