import sys
from collections import Counter
from central_tendency import mean
import math
import statistics

sys.path.append("src/tests")

from test_cleaning import load_data

data = load_data()

# Gets the correlation coefficient to the nearest hundreth
def correlation_coefficient(xData, yData):
    avg_x = mean(xData)
    avg_y = mean(yData)
    dat = [[xData[i], yData[i]] for i in range(0, len(xData))]

    top = sum([(x[0] - avg_x) * (x[1] - avg_y) for x in dat])
    bottom = math.sqrt(sum((x[0] - avg_x) ** 2 for x in dat) * sum((x[1] - avg_y) ** 2 for x in dat))

    return round(top / bottom, 2)


if __name__ == "__main__":
    intDates = [int(row["date"].replace("-", "")) for row in data]
    prices = [row["price"] for row in data]
    print("-- COEFFICIENT DE CORRELATION --")
    print(f"COEFFICIENT: {correlation_coefficient(intDates, prices)}")