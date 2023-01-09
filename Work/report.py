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
            record = dict(zip(headers, row))
            portfolio.append({'name':record['name'], 'shares':int(record['shares']), 'price':float(record['price'])})
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

def make_report(portfolio, prices):
    change_data = []
    for item in portfolio:
        change = prices[item['name']] - item['price']
        change_data.append((item["name"], item["shares"], prices[item["name"]], change))
    return change_data

def print_report(change_data):
    headers = ('Name','Shares','Price','Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for item in change_data:
        price_dollars = "${0}".format(item[2])
        print(f'{item[0]:>10s} {item[1]:>10d} {price_dollars:>10} {item[3]:>10.2f}')

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
change_data = make_report(portfolio, prices)
print_report(change_data)