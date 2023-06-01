import gymnasium as gym
from agent import Boxer


class Game:
    def __init__(self, boxer: Boxer) -> None:
        self.env = gym.make("ALE/Boxing-v5", render_mode="human")
        self.boxer = boxer

    def start(self, step=1000):
        observation, info = self.env.reset(seed=42)
        reward = 0
        for _ in range(step):
            action = self.boxer.take_action(
                observation, reward, info, self.env.action_space)
            step_result = self.env.step(action)
            observation, reward, terminated, truncated, info = step_result
            if terminated or truncated:
                observation, info = self.env.reset()
        self.env.close()
