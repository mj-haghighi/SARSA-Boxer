import pickle
import gymnasium as gym
from agent import Boxer

class Game:
    def __init__(self, boxer: Boxer, start_episode=0) -> None:
        self.env = gym.make("ALE/Boxing-v5")
        self.boxer = boxer
        self.boxer.action_space = self.env.action_space
        self.start_episode = start_episode

    def start(self, episods=3000):
        observation, info = self.env.reset(seed=42)
        reward_history = []
        for e in range(self.start_episode, episods, 1):
            terminated, truncated = False, False
            observation, info = self.env.reset()
            total_reward = 0
            reward = 0
            while not (terminated or truncated):
                action = self.boxer.take_action(observation, reward)
                step_result = self.env.step(action)
                observation, reward, terminated, truncated, info = step_result
                total_reward += reward
            
            print(self.boxer.q_table)
            print(f'episode: {e}, reward: {total_reward}, {self.boxer.params}')

            self.boxer.params.decay_epsilon()
            self.boxer.params.decay_alpha()
            reward_history.append(total_reward)
            
            if e % 10 == 0:
                with open(f'checkpoints/Q2-Table{e}.pickle', 'wb') as handle:
                    pickle.dump(self.boxer.q_table, handle,
                                protocol=pickle.HIGHEST_PROTOCOL)
                with open(f'checkpoints/Rewards.pickle{e}', 'wb') as handle:
                    pickle.dump(reward_history, handle,
                                protocol=pickle.HIGHEST_PROTOCOL)
        self.env.close()

