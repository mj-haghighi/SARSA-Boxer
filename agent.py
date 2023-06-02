import os
import pickle
import numpy as np
from img_utils import find_heads, encode_state


class Boxer:
    """
    Boxer agnet class
    """

    def __init__(self, q_table_path: str) -> None:
        self.q_table = {}
        if q_table_path is not None and os.path.exists(q_table_path):
            self.q_table = pickle.load(q_table_path)
        self.action_space = None

    def take_action(self, observation, reward, info, action_space, episode):
        raise Exception("This method os not imlemented")

    def mine_q_table(self, state):
        if state in self.q_table.keys():
            action, score = np.argmax(self.q_table[state]), np.max(self.q_table[state])
            return action
        return self.action_space.sample()

    def get_score(self, state, action):
        if state in self.q_table.keys():
            return self.q_table[state][action]
        return 0

    def get_q_sum(self):
        total=0
        for key, val in self.q_table.items():
            print(key, np.mean(val), np.max(val))


    def set_score(self, state, action, score):
        if state not in self.q_table.keys():
            self.q_table[state] = np.zeros(shape=(self.action_space.n, ))
        self.q_table[state][action] = score

    def set_action_space(self, actions_space):
        self.action_space = actions_space

    def choose_action(self, state, epsilon=0.1):
        """ Chose action
        """
        action = 0
        if np.random.uniform(0, 1) > epsilon:
            action = self.mine_q_table(state)
        else:
            action = self.action_space.sample()

        return action


class RandomBoxer(Boxer):
    def take_action(self, observation, reward, info, action_space):
        return action_space.sample()


class TrainingBoxer(Boxer):
    def __init__(self, q_table_path: str, resume: bool = False, gamma=0.9, alpha=0.8) -> None:
        super().__init__(q_table_path)
        self.resume = resume
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = 1

        self.state = None
        self.action = None

    def update(self, state, state2, reward, action, action2):
        """
        Function to learn the Q-value
        """

        predict = self.get_score(state, action)
        target = reward + self.gamma * self.get_score(state2, action2)
        score = self.get_score(state, action) + self.alpha * (target - predict)
        self.set_score(state, action, score)

    def take_action(self, observation, reward, info, episode=1):
        boxer, enemy = find_heads(image=observation)
        new_state = encode_state(boxer, enemy)
        self.epsilon = max(0.1, 1 - episode * 0.0005)
        new_action = self.choose_action(new_state, self.epsilon)

        if self.state is not None:
            self.update(self.state, new_state, reward, self.action, new_action)

        self.action = new_action
        self.state = new_state

        return new_action


class FighterBoxer(Boxer):
    pass
