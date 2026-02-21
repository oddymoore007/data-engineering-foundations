import csv

def calculate_average(num_list):
    if len(num_list) == 0:
        return 0

    total = sum(num_list)
    count = len(num_list)
    average = total / count
    return average


def read_sales_data(file_path):
    amounts = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = row["amount"]

            if amount != "":
                amounts.append(float(amount))

    return amounts


file_path = "data/sales.csv"

sales_amounts = read_sales_data(file_path)

average_sales = calculate_average(sales_amounts)

print("Average Sales:", average_sales)