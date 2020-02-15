import gym
import gym_maze
import numpy as np
import dill
dill.settings['recurse'] = True


class Agent:
    def __init__(self, env):
        self.epsilon = 1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.00045
        self.lr_rate = 0.81
        self.gamma = 0.865

        self.observation_space = env.observation_space
        self.action_space = env.action_space
        self.Q = np.zeros(tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int)) + (env.action_space.n,), dtype=float)

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = self.action_space.sample()
        else:
            action = np.argmax(self.Q[state, :])

        return action
    
    def decay_epsilon(self, episode):
        self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * np.exp(-(self.decay_rate * episode))

    def learn(self, state, next_state, reward, action, done):
        predict = self.Q[state, action]

        if done:
            target  = reward
        else:
            target = reward + self.gamma * np.max(self.Q[next_state, :])

        self.Q[state, action] = self.Q[state, action] + self.lr_rate * (target - predict)

    def next_action(self, state):
        action = np.argmax(self.Q[state, :])
        return action

    def state_mapping(self, state):
        state_bounds = list(zip(self.observation_space.low, self.observation_space.high))
        num_buckets = tuple((self.observation_space.high + np.ones(self.observation_space.shape)).astype(int))
        bucket_indice = []
        for i in range(len(state)):
            if state[i] <= state_bounds[i][0]:
                bucket_index = 0
            elif state[i] >= state_bounds[i][1]:
                bucket_index = num_buckets[i] - 1
            else:
                # Mapping the state bounds to the bucket array
                bound_width = state_bounds[i][1] - state_bounds[i][0]
                offset = (num_buckets[i]-1)*state_bounds[i][0]/bound_width
                scaling = (num_buckets[i]-1)/bound_width
                bucket_index = int(round(scaling*state[i] - offset))
            bucket_indice.append(bucket_index)
        return tuple(bucket_indice)


def main():
    env = gym.make('maze-sample-10x10-v0')
    agent = Agent(env)

    episodes = 10
    total_reward = 0


    #env.render()

    for i in range(episodes):
        curr_state = env.reset()
        curr_state = agent.state_mapping(curr_state)

        episode_reward = 0
        done = False

        while not done:
            action = agent.choose_action(curr_state)
            next_state, reward, done, _ = env.step(action)
            next_state = agent.state_mapping(next_state)

            agent.learn(curr_state, next_state, reward, action, done)

            episode_reward += reward
            curr_state = next_state
            #env.render()

        total_reward += episode_reward

        if episode_reward == 1:
            agent.decay_epsilon(i)
        #print(agent.epsilon)
        print(f"{i}) {total_reward}, {episode_reward}, {agent.epsilon}")

    print(total_reward / episodes)
    print(agent.Q)

    env.close()

    save_agent(agent, episodes)


def save_agent(agent, episodes):
    with open(f"test_agents/pickles/GymMaze10x10_QLearning{episodes}.pickle", 'wb') as f:
        dill.dump(agent, f)


if "__main__" == __name__:
    main()
