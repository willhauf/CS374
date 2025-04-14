# testing for Q-learning in Frozen Lake
from environment import FrozenLake
from agent import QLearner
import matplotlib.pyplot as plt
from pickle import dump

agent = QLearner(0.5, 0.99, 0.005, .999)
env = FrozenLake()

batches = 100
episodes = 100
wins = [0] * batches

for batch in range(batches):
    for episode in range(episodes):
        s = env.reset()
        terminal = False

        while not terminal:
            a = agent.choose(s, env.actions)
            r, sp, terminal = env.step(a)
            agent.update(s, a, r, sp, env.actions, terminal)
            s = sp

        if env.current == env.goal:
            wins[batch] += 1

    print(wins[batch], " wins in batch ", batch)

plt.plot(list(range(batches)), wins)
plt.xlabel("Wins in latest batch")
plt.ylabel("Batches of training")
plt.show()

with open("saved_agent.pkl", "wb") as file:
    dump(agent, file)
