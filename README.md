# SARSA-Boxer
This GitHub repository provides an implementation of the Sarsa algorithm for training an agent to interact with the Gymnasium Box environment. The Sarsa algorithm is a reinforcement learning technique that enables the agent to learn optimal actions in an environment through trial and error.



## Lessons Learned

By working on a Reinforcement Learning (RL) project using the SARSA algorithm to train a boxer agent from the Gymnasym AI library, I have likely gained valuable insights and experiences. Throughout this project, I would have learned the intricacies of implementing SARSA, a temporal-difference RL algorithm, to enable the agent to learn and improve its boxing skills iteratively. By observing the agent's interactions with the environment and evaluating its actions based on the anticipated rewards, I would have developed a deep understanding of the agent's decision-making process. This project would have provided me with hands-on experience in RL, enabling me to explore the challenges and opportunities involved in training an agent to excel in a specific task, ultimately enhancing my skills in RL algorithms and their applications.

![Reward Plot](https://github.com/mj-haghighi/SARSA-Boxer/blob/main/plots/reward-plot.png)

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd SARSA-Boxer/
```

Install dependencies

```bash
  pip install gymnasium[atari]
  pip install gymnasium[accept-rom-license]
  pip install opencv-python
  pip install matplotlib
```

Start training:

```bash
  python main.py --train
```
If you want to resume training:

```bash
  python main.py --train --resume --q_table <path-to-Qtable> --start_episode=<start from that episide : int>
```
## Roadmap

- Better feature ectraction from observation space (scene image).

- Write scheduling algorithem for hyperparameters.

- Complete inference script.

- Everythings you know best!


## Authors

- [@mj-haghighi](https://www.github.com/mj-haghighi)


## Contributing

Contributions are always welcome!
