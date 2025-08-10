# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:27:47 2025.

@author: Archik
"""

import gym
import random
import numpy as np
from IPython.display import clear_output
from time import sleep

random.seed(1000)

streets = gym.make("Taxi-v3", render_mode='ansi').env
# New versions keep getting released; if -v3 doesn't work, try -v2 or -v4
print(streets.reset())
streets.render()
initial_state = streets.encode(2, 3, 2, 0)

streets.s = initial_state

streets.render()
streets.P[initial_state]

q_table = np.zeros([streets.observation_space.n, streets.action_space.n])

learning_rate = 0.1
discount_factor = 0.6
exploration = 0.1
epochs = 10000

for taxi_run in range(epochs):
    state, info = streets.reset()
    done = False

    while not done:
        random_value = random.uniform(0, 1)
        if (random_value < exploration):
            action = streets.action_space.sample()
            # Explore a random action
        else:
            action = np.argmax(q_table[state])
            # Use the action with the highest q-value

        next_state, reward, done, done2, info = streets.step(action)

        prev_q = q_table[state, action]
        next_max_q = np.max(q_table[next_state])
        new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
        q_table[state, action] = new_q

        state = next_state



for tripnum in range(1, 11):
    state, info = streets.reset()

    done = False
    trip_length = 0

    while not done and trip_length < 25:
        action = np.argmax(q_table[state])
        next_state, reward, done, done1, info = streets.step(action)
        clear_output(wait=True)
        print("Trip number " + str(tripnum) + " Step " + str(trip_length))
        print(streets.render())
        sleep(.5)
        state = next_state
        trip_length += 1

    sleep(2)
