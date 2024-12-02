import sys
from collections import Counter
import os

sys.path.append(os.path.abspath("src/tests"))

from test_cleaning import load_data

data = load_data()

# Calculates the mode of the given dataset
def mode(dat):
    count = Counter(dat)
    return count.most_common()[0][0]

# Calculates the average of the given dataset to the nearest hundreth
def mean(dat):
    return round(sum(dat) / len(dat), 2)

# Calculates the median of the given dataset to the nearest hundreth
def median(dat):
    dat = sorted(dat)
    length = len(dat)
    middle_index = length // 2

    # List has an even length, calculate middle of two indexes
    if length % 2 == 0:
        return round((dat[middle_index - 1] + dat[middle_index]) / 2, 2)
    else:
        return round(dat[middle_index] / 2, 2)


if __name__ == "__main__":
    prices = [row["price"] for row in data]
    print("-- TENDANCES CENTRALE PRIX --")
    print(f"MODE : {mode(prices)}")
    print(f"MÉDIANE : {median(prices)}")
    print(f"MOYENNE : {mean(prices)}")
