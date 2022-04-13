# Import libraries
import pandas as pd


def read_california_house_prices_data():
    house_prices_data = pd.read_csv('./californiahouseprices/train.csv')
    print(house_prices_data.head())


if __name__ == '__main__':
    read_california_house_prices_data()