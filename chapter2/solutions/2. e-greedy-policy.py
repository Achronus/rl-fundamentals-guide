import numpy as np
import gymnasium as gym


def e_greedy_policy(env: gym.Env, value_table: np.ndarray, state: int, epsilon: float = 0.9) -> int:
    """
    An example of an epsilon-greedy policy.
    
    :param env: (gymnasium.Env) the active gymnasium environment
    :param value_table: (numpy.array) an array of state-value or action-value function approximations
    :param state: (int) the current state index
    :param epsilon: (float) the starting value for the decay rate
    """
    greedy_prob = np.random.randint(low=0, high=1, size=1)

    if greedy_prob < epsilon:
        # Random action
        return env.action_space.sample()
    else:
        # Greedy action
        return np.max(value_table[state])


value_table = np.array([3, 3])
epsilon = 0.9

env = gym.make("LunarLander-v2", render_mode="human")
state, info = env.reset(seed=42)


for _ in range(1000):
   action = e_greedy_policy(env, value_table, state, epsilon)

   state, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()