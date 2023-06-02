class Hyperparameters:
    def __init__(self, gamma, alpha, epsilon) -> None:
        self.epsilon = Hyperparameter(value=epsilon, decayrate=0.0007)
        self.alpha = Hyperparameter(value=alpha, decayrate=0.0005)
        self.gamma = Hyperparameter(value=gamma, decayrate=0.0001)

    def decay_epsilon(self):
        self.epsilon.value = max(0.1, self.epsilon.value - self.epsilon.decayrate)

    def decay_alpha(self):
        self.alpha.value = max(0.15, self.alpha.value - self.alpha.decayrate)

    def decay_gamma(self):
        self.gamma.value = max(0.1, self.gamma.value - self.gamma.decayrate)

    def __str__(self) -> str:
        return f"Gamma: {self.gamma.value} | Alpha: {self.alpha.value} | Epsilon: {self.epsilon.value}"


class Hyperparameter:
    def __init__(self, value, decayrate) -> None:
        self.value = value
        self.decayrate = decayrate
