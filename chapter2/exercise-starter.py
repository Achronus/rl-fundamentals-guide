import numpy as np
import gymnasium as gym


def greedy_policy(value_table: np.ndarray, state: int) -> int:
    """
    An example of a greedy policy.
    
    :param value_table: (numpy.array) an array of state-value or action-value function approximations
    :param state: (int) the current state index
    """
    # Insert code here ...
    pass


def e_greedy_policy(env: gym.Env, value_table: np.ndarray, state: int, epsilon: float = 0.9) -> int:
    """
    An example of an epsilon-greedy policy.
    
    :param env: (gymnasium.Env) the active gymnasium environment
    :param value_table: (numpy.array) an array of state-value or action-value function approximations
    :param state: (int) the current state index
    :param epsilon: (float, optional) the starting value for the decay rate. Defaults to 0.9
    """
    # Insert code here ...
    pass


value_table = np.array([3, 3])
epsilon = 0.9

env = gym.make("LunarLander-v2", render_mode="human")
state, info = env.reset(seed=42)


for _ in range(1000):
   action = greedy_policy(value_table, state)
   # action = e_greedy_policy(env, value_table, state, epsilon)

   state, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()