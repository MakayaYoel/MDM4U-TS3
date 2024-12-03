from collections import Counter
from central_tendency import mean
import math

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
