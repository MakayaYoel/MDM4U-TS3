import sys
from collections import Counter
from central_tendency import mean
import math

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

# Returns the slope of the linear regression line
def linear_regression_slope(xData, yData):
    avgX = mean(xData)
    avgY = mean(yData)

    mean_of_products = sum(xData[i] * yData[i] for i in range(len(xData))) / len(xData)
    top = mean_of_products - avgX * avgY

    mean_of_squares = sum(x ** 2 for x in xData) / len(xData)
    bottom = mean_of_squares - avgX ** 2

    return round(top / bottom, 2)

# Returns the y-intercept/origin of the linear regression line
def linear_regression_origin(xData, yData):
    slope = linear_regression_slope(xData, yData)
    meanY = mean(yData)
    meanX = mean(xData)

    return round(meanY - slope * meanX, 2)

if __name__ == "__main__":
    intDates = [int(row["date"].replace("-", "")) for row in data]
    prices = [row["price"] for row in data]
    print("-- COEFFICIENT DE CORRELATION --")
    print(f"COEFFICIENT: {correlation_coefficient(intDates, prices)}")
    print(f"ÉQUATION DE LA RÉGRESSION: y = {linear_regression_slope(intDates, prices)}x + {linear_regression_origin(intDates, prices)}")
