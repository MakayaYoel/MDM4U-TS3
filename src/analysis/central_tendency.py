import sys
from collections import Counter

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Calculates the mode of prices
def mode():
    prices = [row["price"] for row in data]
    count = Counter(prices)

    return count.most_common()[0][0]

# Calculates the average price to the nearest hundreth
def mean():
    prices = [row["price"] for row in data]

    return round(sum(prices) / len(prices), 2)

# Calculates the median of prices to the nearest hundreth
def median():
    sorted_prices = sorted([row["price"] for row in data])
    length = len(sorted_prices)
    middle_index = length // 2

    # List has an even length, calculate middle of two indexes
    if length % 2 == 0:
        return round((sorted_prices[middle_index - 1] + sorted_prices[middle_index]) / 2, 2)
    else:
        return round(sorted_prices[middle_index] / 2, 2)


if __name__ == "__main__":
    print("-- TENDANCES CENTRALE --")
    print(f"MODE : {mode()}")
    print(f"MÉDIANE : {median()}")
    print(f"MOYENNE : {mean()}")
