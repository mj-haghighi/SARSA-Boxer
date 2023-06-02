import pickle
import gymnasium as gym
from agent import Boxer


class Game:
    def __init__(self, boxer: Boxer) -> None:
        self.env = gym.make("ALE/Boxing-v5")
        self.boxer = boxer
        self.boxer.set_action_space(self.env.action_space)

    def start(self, episods=2000):
        observation, info = self.env.reset(seed=42)
        reward_history = []
        for i in range(episods):
            terminated, truncated = False, False
            observation, info = self.env.reset()
            total_reward = 0
            reward = 0
            step = 0
            while not (terminated or truncated):
                action = self.boxer.take_action(
                    observation, reward, self.env.action_space, i)
                step_result = self.env.step(action)
                observation, reward, terminated, truncated, info = step_result
                total_reward += reward
                step += 1
            reward_history.append(total_reward)
            
            self.boxer.get_q_sum()
            print(f'episode: {i}, reward: {total_reward}, epsilon: {self.boxer.epsilon}')
            
        self.env.close()
        with open('Q2-Table.pickle', 'wb') as handle:
            pickle.dump(self.boxer.q_table, handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

        print(reward_history)
