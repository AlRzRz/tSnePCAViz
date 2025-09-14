import matplotlib.pyplot as plt
import pandas as pd


def main():
    titanic = pd.read_csv('./titanic.csv', index_col=0)
    print(titanic.loc[[12, 23]])






if __name__ == '__main__':
    main()