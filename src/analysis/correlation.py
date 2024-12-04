from collections import Counter
from central_tendency import mean
import math
import datetime
import sys

sys.path.append("src/tests")
from test_cleaning import load_data

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

    top = sum((x - avgX) * (y - avgY) for x, y in zip(xData, yData))
    bottom = sum((x - avgX) ** 2 for x in xData)

    return top / bottom

# Returns the y-intercept/origin of the linear regression line
def linear_regression_origin(xData, yData):
    slope = linear_regression_slope(xData, yData)
    meanY = mean(yData)
    meanX = mean(xData)

    print(f"slope: {slope}, meanY: {meanY}, meanX: {meanX}"	)

    return round(meanY - slope * meanX, 2)

import statistics

data = load_data()

# use days from 2020-01-01 as x values
boeuf_dates = [(datetime.datetime.strptime(row["date"], "%Y-%m") - datetime.datetime(2020, 1, 1)).days for row in data if row["product"] == "Boeuf à ragoût, par kilogramme"]
boeuf_prices = [row["price"] for row in data if row["product"] == "Boeuf à ragoût, par kilogramme"]

print(linear_regression_slope(boeuf_dates, boeuf_prices))
print(linear_regression_origin(boeuf_dates, boeuf_prices))
print(statistics.linear_regression(boeuf_dates, boeuf_prices))
