import sys
from collections import Counter
from central_tendency import mean, median
import math
import statistics

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Returns the range
def stats_range(data):
    return round(max(data) - min(data), 2)

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

# Credit: https://www.calculatorsoup.com/calculators/statistics/percentile-calculator.php
def percentile(data, x):
    sorted_data = sorted(data)
    r = (x / 100) * (len(sorted_data) - 1) + 1

    if r.is_integer():
        return sorted_data[int(r)]
    else:
        integer_part = int(r)
        fractional_part = r - integer_part
        return sorted_data[integer_part - 1] + fractional_part * (sorted_data[integer_part] - sorted_data[integer_part - 1])

def interpercentile_range(data):
    return percentile(data, 75) - percentile(data, 25)

if __name__ == "__main__":
    prices = [row["price"] for row in data]

    print("-- DISPERSION PAR RAPPORT AUX PRIX -- ")
    print(f"ÉTENDUE: {stats_range(prices)}")
    print(f"VARIANCE: {variance(prices)}")
    print(f"ÉCART-TYPE: {standard_deviation(prices)}")
    print(f"QUARTILE 1: {percentile(prices, 25)}")
    print(f"QUARTILE 2: {percentile(prices, 50)}")
    print(f"QUARTILE 3: {percentile(prices, 75)}")
    print(f"INTERVALLE INTERQUARTILE: {interpercentile_range(prices)}")