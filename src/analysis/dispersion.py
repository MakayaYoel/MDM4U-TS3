import sys
from collections import Counter
from central_tendency import mean
import math
import statistics

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Returns the range
def stats_range(data):
    return max(data) - min(data)

TYPE_POPULATION = 0
TYPE_SAMPLE = 1

# Calculates the variance of the given dataset
def variance(data, type=TYPE_SAMPLE):
    avg = mean(data)

    top_sum = sum([(price - avg) ** 2 for price in data])

    return round(top_sum / (len(data) - type), 2)

# Calculates the standard deviation of the dataset
def standard_deviation(data, type=TYPE_SAMPLE):
    return round(math.sqrt(variance(data, type)), 2)

# Gets the Z Score of a specified point
def z_score(data, x) :
    return (x - mean(data)) / standard_deviation()

if __name__ == "__main__":
    prices = [row["price"] for row in data]
    print("-- DISPERSION PAR RAPPORT AUX PRIX -- ")
    print(f"ÉTENDUE: {stats_range(prices)}")
    print(f"VARIANCE: {variance(prices)}")
    print(f"ÉCART-TYPE: {standard_deviation(prices)}")