import pickle


class Boxer:
    """
    Boxer agnet class
    """

    def __init__(self, q_table_path: str) -> None:
        self.q_table = pickle.load(q_table_path)

    def train(self, resume: bool = False) -> None:
        """
        Train boxer
        inputs:
            resume: to resume training, load Q-table and continue training.
        """
        pass

    def fight(self) -> None:
        """ Start to fight
        """
        pass
