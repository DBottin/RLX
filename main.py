import gym

env = gym.make("Ant-v4")
observation = env.reset()

for _ in range(10000):

  env.render()
  action = env.action_space.sample()
  observation, reward, done, info = env.step(action)

  if (_ % 100 == 0):
    print(observation)
    print(reward)
    print(info)

env.reset()

env.close()