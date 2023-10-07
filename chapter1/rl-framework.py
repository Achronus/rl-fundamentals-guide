import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")  # Create an environment
state, info = env.reset(seed=42)  # Set the first state

# Iterate through the environment 1000x
for i_episode in range(1000):
    action = policy(state, actions=env.action_space)  # Generate an action using a policy
    state, reward, terminal, truncated, info = env.step(action)  # Observe the environment

    # Check if episode has ended
    if terminal or truncated:
        state, info = env.reset()  # Reset environment for next episode

env.close()  # Exit environment
