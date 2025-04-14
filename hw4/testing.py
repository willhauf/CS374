# testing for Q-learning in Frozen Lake\

from hw4.environment import FrozenLake
from hw4.agent import QLearner
import matplotlib.pyplot as plt
from pickle import dump
import time

agent = QLearner(0.5, 0.99, 0.005, .999, 13)
env = FrozenLake()

batches = 100
episodes = 100
wins = [0] * batches

for batch in range(batches):
    for episode in range(episodes):
        s = env.reset()
        terminal = False
        # Limit the time for each episode to 15 seconds
        start_time = time.time()
        time_limit = 5  # seconds

        while not terminal:
            if time.time() > start_time + time_limit:
                terminal = True
            a = agent.choose(s, env.actions)
            r, sp, terminal = env.step(a)
            agent.update(s, a, r, sp, env.actions, terminal)
            s = sp

        if env.current == env.goal:
            wins[batch] += 1

    print(wins[batch], "% wins in batch ", batch)

plt.plot(list(range(batches)), wins)
plt.xlabel("Wins in latest batch")
plt.ylabel("Batches of training")
plt.show()

with open("saved_agent.pkl", "wb") as file:
    dump(agent, file)
