import gym
import dill
dill.settings['recurse'] = True


class Agent:
    def __init__(self, env):
        self.action_space = env.action_space

    def next_action(self, state):
        return self.action_space.sample()


def main():
    env = gym.make('FrozenLake-v0')
    agent = Agent(env)

    episodes = 10000
    total_reward = 0

    for i in range(episodes):
        curr_state = env.reset()
        episode_reward = 0
        done = False

        while not done:
            # env.render()
            action = agent.next_action(curr_state)
            next_state, reward, done, info = env.step(action)

            episode_reward += reward
            curr_state = next_state

        total_reward += episode_reward
        # env.render()

    print(total_reward / episodes)

    env.close()

    save_agent(agent)


def save_agent(agent):
    with open(f"FrozenLake_RandomAgent.pickle", 'wb') as f:
        dill.dump(agent, f)


if "__main__" == __name__:
    main()
