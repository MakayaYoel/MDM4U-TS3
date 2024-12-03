from collections import Counter

# Calculates the mode of the given dataset
def mode(data):
    count = Counter(data)
    return count.most_common()[0][0]

# Calculates the average of the given dataset to the nearest hundreth
def mean(data):
    return round(sum(data) / len(data), 2)

# Calculates the median of the given dataset to the nearest hundreth
def median(data):
    data = sorted(data)
    length = len(data)
    middle_index = length // 2

    # List has an even length, calculate middle of two indexes
    if length % 2 == 0:
        return round((data[middle_index - 1] + data[middle_index]) / 2, 2)
    else:
        return round(data[middle_index] / 2, 2)
