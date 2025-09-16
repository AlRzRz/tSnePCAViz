import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time




# [x] Implementation of a random walk func to simulate a trader's pot size based on his win-rate (hacker statistics basically)
def randomWalkDownWallSt(winRate, trades, potsize, riskToReward, multiplier, seed):
    
    win = multiplier * riskToReward
    loss = multiplier

    potTracker = [potsize]

    np.random.seed(seed=seed)

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

    seed = int(time.time())

    for _ in range(numSimulations):


        simulations.append(randomWalkDownWallSt(winRate=winrate, trades=trades, potsize=potsize, riskToReward=riskToReward, multiplier=multiplier, seed=seed))
        seed += 1

    print(simulations[1][:10])
    
    # We can see that this plots 15001 lines (in the situation I tested, X amount of lines in general) for each simulation. Basically, for each second of the simulation, it plots a line that
    # connects all the simulations positions at that second. Instead we need to find the lines for each simulation plotted through all the seconds. Numpy works by making a line for each feature.
    # Therefore we need Y features (basically the num. of simulations, 20 in this current moment that I tested this code). This way, it should go through 15001 rows (observations at different seconds)
    # for 5 different lines (each line signifying a simulation. Therefore we need to perform a transverse operation on the matrix to switch the rows and colums: basically go from (y, x) to (x, y))
    np_sims = np.array(simulations)
    print(np_sims.shape)
    print(np_sims[1][:10])

    np_sims_t = np_sims.transpose()
    print(np_sims_t.shape)

    print(np_sims_t[0:3])
    
    fig, ax = plt.subplots()
    ax.plot(np_sims_t)
    ax.set_title('Portfolio Simultaions')
    ax.set_xlabel('Trades (#)')
    ax.set_ylabel('Portfolio Value ($)')
    plt.show()




if __name__ == "__main__":

    WINRATE = 0.85
    RISKTOREWARD = 3
    POTSIZE = 3000
    TRADES = 1000
    MULTIPLIER = 1000
    NUM_SIMULATIONS = 30

    print('\n', 'APPLICATION HAS INITIALIZED'.center(35, '-'), '\n')
    print(f"""
CURRENT VARIABLES:
        WINRATE - ONLY ASSIGN FLOAT SYMBOLIZING A PERCENTAGE: {WINRATE}
        RISK-REWARD (RR) - INT: {RISKTOREWARD}
        POTSIZE - INT: {POTSIZE}
        TRADES - INT: {TRADES}
        MULTIPLIER - INT: {MULTIPLIER}
        NUMBER OF SIMULATIONS (NUM_SIMS) - INT: {NUM_SIMULATIONS}
""")
    
    while True:
        valid_resps = ['winrate', 'rr', 'potsize', 'trades', 'multiplier', 'num_sims']

        user_resp = input('Would you like to change any of these starting variables? If so, please indicate so by writing its corresponding name (or the name in-between parentheses if present). Please indicate any variation of the word "quit" to exit:\n').lower()
        print()
        if user_resp.lower() == 'quit':
            break
        elif user_resp.lower() not in valid_resps:
            continue

        indexOfTarget = valid_resps.index(user_resp)

        while True:
            changeToResp = float(input(f'What would you like to change {user_resp.upper()} to? (DOUBLE CHECK RECOMMEND DATA TYPE TO AVOID THE PROGRAM CRASHING!)\n'))
            print()
            # if not isinstance(changeToResp, int) and not isinstance(changeToResp, float):
            #     print('Please provide a valid int/float as the data type.\n')
            #     continue

            # [x] Assign variable here and break

            if indexOfTarget == 0:
                WINRATE = changeToResp
            elif indexOfTarget == 1:
                RISKTOREWARD = changeToResp
            elif indexOfTarget == 2:
                POTSIZE = changeToResp
            elif indexOfTarget == 3:
                TRADES = changeToResp
            elif indexOfTarget == 4:
                MULTIPLIER = changeToResp
            elif indexOfTarget == 5:
                NUM_SIMULATIONS = changeToResp
            break


    print("\nSTARTING APPLICATION WITH:".center(35, '='), '\n')
    print(f"""
FINAL VARIABLES:
        WINRATE: {WINRATE}
        RISK-REWARD (RR): {RISKTOREWARD}
        POTSIZE: {POTSIZE}
        TRADES: {TRADES}
        MULTIPLIER: {MULTIPLIER}
        NUMBER OF SIMULATIONS (NUM_SIMS): {NUM_SIMULATIONS}
""")




    
    # main(winrate=WINRATE, trades=TRADES, potsize=POTSIZE, riskToReward=RISKTOREWARD, multiplier=MULTIPLIER, numSimulations=NUM_SIMULATIONS)
    