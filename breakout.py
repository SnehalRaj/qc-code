import gym
import time
env = gym.make('Breakout-v0')
env.reset()
for _ in range(5000):
    env.render()
    action = env.action_space.sample() # take a random action
    observation, reward, done, info = env.step(action)
