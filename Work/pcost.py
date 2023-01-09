# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total += (shares * price)
            except ValueError:
                print(f"Row {i}: Couldn't convert: {row}")
    print(f'Total cost {round(total,2)}')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
portfolio_cost(filename)