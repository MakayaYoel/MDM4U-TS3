import csv
from datetime import datetime
import os

def test_cleaning():
    raw_file_path = 'data/raw/1810024501_donneesselectionnees.csv'
    cleaned_file_path = 'data/cleaned/cleaned_data.csv'
    
    # Make sure dirs exists
    os.makedirs(os.path.dirname(cleaned_file_path), exist_ok=True)

    data = load_data()
    save_cleaned_data(data, cleaned_file_path)
        

def extract_relevant_data(row):
    date = row[0]
    product = row[3]
    price = float(row[10])
    
    return {"date": date, "product": product, "price": price}

def save_cleaned_data(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvFile:
        headers = ['date', 'product', 'price']
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def load_data() :
    raw_file_path = 'data/raw/1810024501_donneesselectionnees.csv'
    cleaned_file_path = 'data/cleaned/cleaned_data.csv'
    data = []

    # need utf-8 encoding cause french/latin characters
    with open(raw_file_path, encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=';', quotechar="|")
        

        """
            Indexes
            --------
            0 : Date
            3 : Product
            4 : Unit of mesure
            10 : Price
        """

        for i, row in enumerate(reader):
            row = [r.replace('"', '') for r in row]

            if i == 0 or len(row) == 0 or row[4] != "Dollars":
                continue

            data.append(extract_relevant_data(row))
    
    return data

if __name__ == "__main__":
    test_cleaning()
