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

    top = sum((x - avgX) * (y - avgY) for x, y in zip(xData, yData))
    bottom = sum((x - avgX) ** 2 for x in xData)

    return top / bottom

# Returns the y-intercept/origin of the linear regression line
def linear_regression_origin(xData, yData):
    slope = linear_regression_slope(xData, yData)
    meanY = mean(yData)
    meanX = mean(xData)

    return round(meanY - slope * meanX, 2)

from prettytable import PrettyTable
import sys
import os
import datetime

sys.path.append("src/tests")
from test_cleaning import products, load_data

import statistics

if __name__ == "__main__":
    os.makedirs("outputs/tables", exist_ok=True)
    data = load_data()

    table = PrettyTable()
    table.field_names = ["Produit", "Coefficient de corrélation", "Équation de la droite de régression"]

    for product in products:
        prices = [row["price"] for row in data if row["product"] == product]
        dates = [(datetime.datetime.strptime(row["date"], "%Y-%m") - datetime.datetime(2020, 1, 1)).days for row in data if row["product"] == product]

        table.add_row([product, f"{correlation_coefficient(dates, prices):.2f}", f"y = {linear_regression_slope(dates, prices):.4f}x + {linear_regression_origin(dates, prices):.2f}"])
        
    with open("outputs/tables/tableau_correlation_produits.txt", "w", encoding="utf-8") as file:
        file.write(table.get_string())


