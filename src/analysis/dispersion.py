import sys
from collections import Counter
from central_tendency import mean

TYPE_POPULATION = 0
TYPE_SAMPLE = 1

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Returns the range
def stats_range():
    prices = [row["price"] for row in data]
    return max(prices) - min(prices)

# Calculates the variance of prices
def variance(type):
    prices = [row["price"] for row in data]
    average_price = mean()
    rmv = 0 if type == TYPE_POPULATION else 1

    top_sum = sum((price - average_price) ** 2 for price in prices)

    return round(top_sum / (len(prices) - rmv), 2)






if __name__ == "__main__":
    print(variance())