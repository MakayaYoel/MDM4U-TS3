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


import sys
import os
from prettytable import PrettyTable

sys.path.append("src/tests")
from test_cleaning import products, load_data

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    data = load_data()
    table = PrettyTable()
    table.field_names = ["Produit", "Mode", "Moyenne", "Médiane"]
    for product in products:
        product_data = [row["price"] for row in data if row["product"] == product]
        table.add_row([product, str(mode(product_data)) + " $", str(mean(product_data)) + " $", str(median(product_data)) + " $"])
    with open("outputs/tableau_tendence_centrales_produits.txt", "w", encoding="utf-8") as file:
        file.write(table.get_string())
