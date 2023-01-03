# pcost.py
#
# Exercise 1.27

total = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        total += float(line.split(',')[-1])
print(f'Total cost {round(total,2)}')