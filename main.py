import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def nameDoubled(name):
    return len(name) * 2



def main():
    titanic = pd.read_csv('./titanic.csv', index_col=0)


    titanic['name length'] = titanic['Name'].apply(nameDoubled)
    print(titanic)


    # for label, row in titanic.iterrows():
    #     print(f'Label: {label}')
    #     print(row)




if __name__ == '__main__':
    main()