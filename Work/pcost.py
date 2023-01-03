# pcost.py
#
# Exercise 1.27
import csv
def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total += (shares * price)
            except ValueError:
                print(f'line {row} cannot be parsed for a share and/or price')
    print(f'Total cost {round(total,2)}')

#portfolio_cost('Data/portfolio.csv')