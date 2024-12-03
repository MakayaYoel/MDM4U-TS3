import matplotlib.pyplot as plt
import os
import numpy as np
import sys
import math
import datetime
from correlation import linear_regression_slope, linear_regression_origin

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

def distribution_of_prices(product_name, start_date: str, end_date: str):
    plt.figure(figsize=(10, 5))
    prices = [row["price"] for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)]
    plt.hist(prices, edgecolor='black', bins=3, color='skyblue')
    plt.title(f"Distribution des prix de {product_name} entre {start_date} et {end_date}", fontsize=10)
    plt.xlabel("Prix ($)")
    plt.ylabel("Fréquence")
    plt.savefig(f"outputs/{product_name}_distribution_of_prices_{start_date}_{end_date}.png")
    plt.close()

def price_trends(product_name, start_date: str, end_date: str):
    plt.figure(figsize=(16, 5))
    filtered_data = [row for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)]

    prices = [row["price"] for row in filtered_data]
    xPoints = [datetime.datetime.strptime(row["date"], "%Y-%m").strftime("%b %y") for row in filtered_data]
    
    plt.plot(xPoints, prices)
    plt.title(f"Tendances des prix de {product_name} entre {start_date} et {end_date}", fontsize=10)
    plt.xlabel("Mois")
    plt.ylabel("Prix ($)")
    plt.savefig(f"outputs/{product_name}_price_trends_{start_date}_{end_date}.png")
    plt.close()

def plot_regression_line(product_name, start_date: str, end_date: str):
    plt.figure(figsize=(10, 5))
    filtered_data = [row for row in data if row["product"] == product_name and is_valid_date(row["date"], start_date, end_date)]
    prices = [row["price"] for row in filtered_data]
    dates = [datetime.datetime.strptime(row["date"], "%Y-%m") for row in filtered_data]
    
    dates_numeric = [d.timestamp() for d in dates]
    
    slope = linear_regression_slope(dates_numeric, prices)
    intercept = linear_regression_origin(dates_numeric, prices)
    line_x = np.array([min(dates_numeric), max(dates_numeric)])
    line_y = slope * line_x + intercept
    
    line_x_dates = [datetime.datetime.fromtimestamp(x) for x in line_x]
    
    plt.scatter(dates, prices, color='blue', alpha=0.5)  # Add scatter plot of actual data
    plt.plot(line_x_dates, line_y, 'r', label=f'y = {slope:.2f}x + {intercept:.2f}')
    plt.legend()
    plt.title(f"Régression linéaire des prix de {product_name} entre {start_date} et {end_date}", fontsize=10)
    plt.xlabel("Date")
    plt.ylabel("Prix ($)")
    plt.savefig(f"outputs/{product_name}_regression_line_{start_date}_{end_date}.png")
    plt.close()
