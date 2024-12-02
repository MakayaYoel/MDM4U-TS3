import sys
from collections import Counter
from central_tendency import mean
import math

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Returns the range
def stats_range():
    prices = [row["price"] for row in data]
    return max(prices) - min(prices)

TYPE_POPULATION = 0
TYPE_SAMPLE = 1

# Calculates the variance of prices
def variance(type):
    prices = [row["price"] for row in data]
    average_price = mean()

    top_sum = sum((price - average_price) ** 2 for price in prices)

    return round(top_sum / (len(prices) - type), 2)

# Calculates the standard deviation of the dataset
def standard_deviation():
    return round(math.sqrt(variance(TYPE_SAMPLE)), 2)

# Gets the Z Score of a specified point
def z_score(x) :
    return (x - mean()) / standard_deviation()

if __name__ == "__main__":
    print("-- DISPERSION -- ")
    print(f"ÉTENDUE: {stats_range()}")
    print(f"VARIANCE: {variance(TYPE_SAMPLE)}")
    print(f"ÉCART-TYPE: {standard_deviation()}")