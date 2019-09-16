import dill
import gym

from .. import db

def evaluate_agent(agent):
    env = gym.make('FrozenLake-v0')

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

    return total_reward / episode

def validate_pickle(pickled_agent):
    
    # Load agent instance from bytestream
    agent = dill.loads(pickled_agent)

    # Validate that the agent instance has next_action attribute and class Agent
    if "Agent" in repr(agent) and hasattr(agent, "next_action"):
        return agent
    else:
        raise Exception("Pickle file does not containt an agent of class 'Agent' or does not have next_action method.")


def submit_agent(student_id, agent):
    return "Yes!"

def save_to_db(name):
    db.db.environments.insert_one({ "name": name })