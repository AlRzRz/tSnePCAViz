import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time




# [x] Implementation of a random walk func to simulate a trader's pot size based on his win-rate (hacker statistics basically)
def randomWalkDownWallSt(winRate, trades, potsize, riskToReward, multiplier):
    
    win = multiplier * riskToReward
    loss = multiplier

    potTracker = [potsize]

    np.random.seed(int(time.time()))

    for _ in range(trades):
        rand0To1 = np.random.rand()

        if rand0To1 <= winRate:
            potTracker.append(potTracker[-1] + win)
        else:
            potTracker.append(potTracker[-1] - loss)

    return potTracker

    # fig, ax = plt.subplots()

    # ax.plot(potTracker)
    # ax.set_title('Portfolio Simulations')
    # ax.set_xlabel('Trades (#)')
    # ax.set_ylabel('Portfolio Value ($)')
    # plt.show()

    # plt.plot(potTracker)
    # plt.title('Portfolio Simulation', fontweight='bold')
    # plt.show()



def main(winrate, trades, potsize, riskToReward, multiplier, numSimulations):
    
    simulations = []

    for _ in range(numSimulations):
        simulations.append(randomWalkDownWallSt(winRate=winrate, trades=trades, potsize=potsize, riskToReward=riskToReward, multiplier=multiplier))

    
    # We can see that this plots 15001 lines (in the situation I tested, X amount of lines in general) for each simulation. Basically, for each second of the simulation, it plots a line that
    # connects all the simulations positions at that second. Instead we need to find the lines for each simulation plotted through all the seconds. Numpy works by making a line for each feature.
    # Therefore we need Y features (basically the num. of simulations, 20 in this current moment that I tested this code). This way, it should go through 15001 rows (observations at different seconds)
    # for 5 different lines (each line signifying a simulation. Therefore we need to perform a transverse operation on the matrix to switch the rows and colums: basically go from (y, x) to (x, y))
    np_sims = np.array(simulations)
    print(np_sims.shape)

    np_sims_t = np_sims.transpose()
    print(np_sims_t.shape)

    print(np_sims_t[0:2])
    
    fig, ax = plt.subplots()
    ax.plot(np_sims_t)
    ax.set_title('Portfolio Simultaions')
    ax.set_xlabel('Trades (#)')
    ax.set_ylabel('Portfolio Value ($)')
    plt.show()




if __name__ == "__main__":

    WINRATE = 0.85
    RISKTOREWARD = 3
    POTSIZE = 10000
    TRADES = 15000
    MULTIPLIER = 2000
    NUM_SIMULATIONS = 5
    
    main(winrate=WINRATE, trades=TRADES, potsize=POTSIZE, riskToReward=RISKTOREWARD, multiplier=MULTIPLIER, numSimulations=NUM_SIMULATIONS)
    