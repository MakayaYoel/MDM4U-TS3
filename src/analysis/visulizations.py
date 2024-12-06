import matplotlib.pyplot as plt
import os
import numpy as np
import sys
import math
import datetime
from babel.dates import format_date
from correlation import linear_regression_slope, linear_regression_origin
import seaborn as sns

sys.path.append("src/tests")
import test_cleaning as tc

os.makedirs("outputs", exist_ok=True)

data = tc.load_data()
# Checks if the date is in range of the start and end date
def is_valid_date(date: str, start_date: str, end_date: str) -> bool:
    start_date = datetime.datetime.strptime(start_date, "%Y-%m")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m")
    date_obj = datetime.datetime.strptime(date, "%Y-%m")
    return start_date <= date_obj <= end_date

def price_trends(product_name, start_date: str, end_date: str, figsize: tuple = (36, 8)):
    plt.figure(figsize=figsize)
    filtered_data = [row for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)]

    prices = [row["price"] for row in filtered_data]
    xPoints = [f"{format_date(datetime.datetime.strptime(row['date'], '%Y-%m'), 'MMMM', locale='fr')[:3]}.\n({row['date'][:4]})" for row in filtered_data]

    plt.plot(xPoints, prices)
    plt.title(f"Tendances des prix de {product_name} entre {start_date} et {end_date}", fontsize=12)
    plt.xlabel("Mois\n(Année)")
    plt.ylabel("Prix ($)")
    plt.savefig(f"outputs/price_trends/{product_name}_price_trends_{start_date}_{end_date}.png")
    plt.close()

def plot_regression_line(product_name, start_date: str, end_date: str):
    plt.figure(figsize=(10, 5))
    filtered_data = [row for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)]
    prices = [row["price"] for row in filtered_data]
    dates = [(datetime.datetime.strptime(row["date"], "%Y-%m") - datetime.datetime(2020, 1, 1)).days for row in filtered_data]

    # Individual points
    plt.plot(dates, prices, 'o', color='blue')
    
    slope = linear_regression_slope(dates, prices)
    intercept = linear_regression_origin(dates, prices)

    # Regression line
    plt.plot(dates, slope * np.array(dates) + intercept, label=f'y = {slope:.2f}x + {intercept:.2f}', color='red')

    plt.legend()

    plt.title(f"Régression linéaire des prix de {product_name} entre {start_date} et {end_date}", fontsize=10)
    plt.xlabel("Jours depuis le 1er janvier 2020")
    plt.ylabel("Prix ($)")
    plt.savefig(f"outputs/plots/{product_name}_regression_line_{start_date}_{end_date}.png")
    plt.close()

def hist_plot_with_bell_curve(product_name, start_date: str, end_date: str):
    sns.histplot(data=[row["price"] for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)], kde=True, alpha=0.1, edgecolor=(0, 0, 0, 0.2))
    plt.title(f"Prix de {product_name} entre {start_date} et {end_date}", fontsize=8)
    plt.xlabel("Prix ($)")
    plt.ylabel("Fréquence")
    plt.savefig(f"outputs/histograms/{product_name}_hist_plot_with_bell_curve_{start_date}_{end_date}.png")
    plt.close()

if __name__ == "__main__":
    # create price trends for all products in outputs/price_trends
    os.makedirs("outputs/price_trends/", exist_ok=True)
    os.makedirs("outputs/histograms/", exist_ok=True)
    os.makedirs("outputs/plots/", exist_ok=True)
    for product in tc.products:
        price_trends(product, "2020-01", "2024-12")
        hist_plot_with_bell_curve(product, "2020-01", "2024-12")
        plot_regression_line(product, "2020-01", "2024-12")

    # chicken price seems to have decreased from april to june 2020
    price_trends("Poulet entier, par kilogramme", "2020-04", "2020-06", figsize=(12, 4))

