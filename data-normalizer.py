#!/usr/bin/env python3
"""
This is a script to parse a CSV file from our team's AirTable database into easily analyzable data for Google Data Studio.

Author: Karthik Hari
"""

import sys

file = sys.argv[1]

with open(file, 'r') as f:
    data = f.read()

    # replace all with numbers
    numbered = data.replace(',,', ',0,') \
        .replace('checked', '1') \
        .replace('None', '0') \
        .replace('1. Low Rung', '1') \
        .replace('2. Mid Rung', '2') \
        .replace('3. High Rung', '3') \
        .replace('4. Traversal Rung', '4') \
        .split('\n')

    out = ''

    print(f'parsing {len(numbered)} lines')

    for line in numbered:
        columns = line.split(',')
        if len(columns) == 1:
            continue  # skip empty entries

        # remove all notes since commas are annoying and not useful for broad analysis
        while len(columns) > 8:
            columns.pop()

        # check if the team number and match are swapped
        if (columns[0].isdecimal() and (int(columns[0]) < 100 or int(columns[1]) > 500)):
            t = columns[0]
            columns[0] = columns[1]
            columns[1] = t

        # add in zeroes if the last column is blank
        if columns[7] == '':
            columns[7] = 0

        # put the csv back together
        out += ','.join(columns) + '\n'

# write data
with open(file, 'wb') as f:
    f.write(out.encode('utf-8'))
    print('done!')
