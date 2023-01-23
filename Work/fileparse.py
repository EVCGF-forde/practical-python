# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, *, select=None):
    '''Parse a CSV file into a list of records'''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = None if not select else [c for c, v in enumerate(headers) if v in select]
        if indices:
            headers = [headers[i] for i in indices]
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[i] for i in indices]
            record = dict(zip(headers, row))
            records.append(record)
    return records