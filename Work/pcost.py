# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            fields = line.split(',')
            try:
                shares = int(fields[1])
                price = float(fields[2])
                total += (shares * price)
            except ValueError:
                print(f'line {line} cannot be parsed for a share and/or price')
    print(f'Total cost {round(total,2)}')

#portfolio_cost('Data/portfolio.csv')