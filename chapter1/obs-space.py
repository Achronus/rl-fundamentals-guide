from gymnasium.spaces import Box
import numpy as np

# A single RGB image
observation_space = Box(low=0, high=255, shape=(210, 160, 3), dtype=np.uint8)
