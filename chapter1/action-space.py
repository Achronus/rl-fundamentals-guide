from gymnasium.spaces import Discrete, Box
import numpy as np

# Discrete action space with 3 actions
action_space = Discrete(n=3, start=1, seed=42)  # {1, 2, 3}

# Continuous variant with 1 action (movement speed) ranging from -1.0 -> 1.0
action_space = Box(low=-1.0, high=1.0, shape=(1,), dtype=np.float32, seed=42) 
