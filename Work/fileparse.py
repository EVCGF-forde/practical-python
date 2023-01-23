# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, *, select=None, types=None, has_headers=True, delimiter=','):
    '''Parse a CSV file into a list of records'''
    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        indices = None
        if has_headers:
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
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records