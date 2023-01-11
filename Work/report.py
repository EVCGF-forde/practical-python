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
    report = []
    for item in portfolio:
        change = prices[item['name']] - item['price']
        report.append((item["name"], item["shares"], prices[item["name"]], change))
    return report

def print_report(report):
    headers = ('Name','Shares','Price','Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for item in report:
        price_dollars = "${0}".format(item[2])
        print(f'{item[0]:>10s} {item[1]:>10d} {price_dollars:>10} {item[3]:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    return make_report(portfolio, prices)

#portfolio = read_portfolio('Data/portfoliodate.csv')
#prices = read_prices('Data/prices.csv')
report = portfolio_report('Data/portfoliodate.csv', 'Data/prices.csv')
print_report(report)