import numpy as np
import gymnasium as gym


def greedy_policy(value_table: np.ndarray, state: int) -> int:
    """
    An example of a greedy policy.
    
    :param value_table: (numpy.array) an array of state-value or action-value function approximations
    :param state: (int) the current state index
    """
    return np.max(value_table[state])


value_table = np.array([3, 3])
epsilon = 0.9

env = gym.make("LunarLander-v2", render_mode="human")
state, info = env.reset(seed=42)


for _ in range(1000):
   action = greedy_policy(value_table, state)

   state, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()