import gym
import dill


def main():
    env = gym.make('FrozenLake-v0')

    with open("FrozenLake_QLearning10000.pickle", 'rb') as f:
        agent = dill.load(f)

    episodes = 10000
    total_reward = 0

    for episode in range(episodes):
        curr_state = env.reset()
        episode_reward = 0
        done = False

        while not done:
            action = agent.next_action(curr_state)

            next_state, reward, done, info = env.step(action)
            episode_reward += reward

            curr_state = next_state

        total_reward += episode_reward

    print(total_reward / episodes)


if "__main__" == __name__:
    main()
