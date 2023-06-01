import os
import pickle


class Boxer:
    """
    Boxer agnet class
    """

    def __init__(self, q_table_path: str) -> None:
        self.q_table = None
        if q_table_path is not None and os.path.exists(q_table_path):
            self.q_table = pickle.load(q_table_path)

    def take_action(self, observation, reward, info):
        raise Exception("This method os not imlemented")


class RandomBoxer(Boxer):
    def take_action(self, observation, reward, info, action_space):
        return action_space.sample()


class TrainingBoxer(Boxer):
    def __init__(self, q_table_path: str, resume: bool = False) -> None:
        super().__init__(q_table_path)
        self.resume = resume


class FighterBoxer(Boxer):
    pass
