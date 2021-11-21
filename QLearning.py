import numpy as np
import tensorflow as tf
import my_env
import os

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def main():
    env = my_env.DinoEnv()
    states = (4,)
    actions = env.action_space.n
    model = build_model(states, actions)

    print(model.summary())
    episodes = 25
    for episode in range(1, episodes + 1):
        obs = env.reset()
        done = False
        score = 0
        """
        while not done:
            env.render()
            action = env.action_space.sample()
            print(action)
            obs, reward, done, info = env.step(action)
            score += reward
        print('Episode:{} Score:{}'.format(episode, score))
    env.close()"""
    dqn = build_agent(model, actions)
    dqn.compile(tf.keras.optimizers.Adam(lr=1e-3), metrics = ['mae'])
    dqn.fit(env, nb_steps = 50000, visualize = True, verbose = 1)


def build_model(states, actions):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(24, activation = 'relu', input_shape = states))
    model.add(tf.keras.layers.Dense(24, activation = 'relu'))
    model.add(tf.keras.layers.Dense(actions, activation = 'linear'))
    return model

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory = memory, policy = policy,
        nb_actions = actions, nb_steps_warmup = 10, target_model_update = 1e-2)
    return dqn



if __name__ == "__main__":
    main()