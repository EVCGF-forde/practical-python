# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            temp_dict = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(temp_dict)

    return portfolio

def read_prices(filename):
    price_list = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if not any(row):
                continue
            price_list[row[0]] = float(row[1])
    return price_list

def calculate_change(portfolio, prices):
    portfolio_total = 0
    portfolio_change = 0
    for item in portfolio:
        prev_value = item['shares'] * item['price']
        new_value = item['shares'] * prices[item['name']]
        portfolio_total += new_value
        portfolio_change += round(new_value - prev_value, 2)
    return(portfolio_total, portfolio_change)

