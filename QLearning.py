import numpy as np
import my_env
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def main():
    env = my_env.DinoEnv()
    states = env.observation_space.shape[0]
    print(env.observation_space.shape)
    print(states)
    actions = env.action_space.n
    print(actions)
    model = build_model(states, actions)

    print(model.summary())
    episodes = 25
    """
    for episode in range(1, episodes + 1):
        obs = env.reset()
        done = False
        score = 0
        while not done:
            env.render()
            action = env.action_space.sample()
            print(action)
            obs, reward, done, info = env.step(action)
            score += reward
        print('Episode:{} Score:{}'.format(episode, score))
    env.close()"""
    dqn = build_agent(model, actions)
    dqn.compile(Adam(lr=1e-3), metrics = ['mae'])
    dqn.get_config()
    dqn.fit(env, nb_steps = 50000, visualize = True, verbose = 2)


def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape = (1, states)))
    model.add(Dense(24, activation = 'relu'))
    model.add(Dense(24, activation = 'relu'))
    model.add(Dense(actions, activation = 'linear'))
    return model

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory = memory, policy = policy,
        nb_actions = actions, nb_steps_warmup = 10, target_model_update = 1e-2)
    return dqn



if __name__ == "__main__":
    main()