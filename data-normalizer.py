#!/usr/bin/env python3
"""
A script to parse a CSV file from our team's AirTable database into easily analyzable data for Google Data Studio.
"""

__author__ = "Karthik Hari"
__version__ = "0.1.0"
__license__ = "CC0-1.0"

import sys

def main(file):
    with open(file, 'r') as f:
        data = f.read()

        # Replace human-readable input w/ numbers
        numbered = data.replace(',,', ',0,') \
            .replace('checked', '1') \
            .replace('None', '0') \
            .replace('1. Low Rung', '1') \
            .replace('2. Mid Rung', '2') \
            .replace('3. High Rung', '3') \
            .replace('4. Traversal Rung', '4') \
            .split('\n')

        out = ''

        print(f'Parsing {len(numbered)} Lines...')

        for line in numbered:
            columns = line.split(',')
            if len(columns) == 1:
                continue  # Skip empty entries

            # Remove all notes since commas are not useful for broad analysis
            while len(columns) > 8:
                columns.pop()

            # Check if team number and match are swapped
            if (columns[0].isdecimal() and (int(columns[0]) < 100 or int(columns[1]) > 500)):
                t = columns[0]
                columns[0] = columns[1]
                columns[1] = t

            # Add zeroes if last column is blank
            if columns[7] == '':
                columns[7] = 0

            # Put csv back together
            out += ','.join(columns) + '\n'

    # Write data as bytes
    with open(file, 'wb') as f:
        f.write(out.encode('utf-8'))
        print('Done!')


if __name__ == "__main__":
    # Take args
    try:
        file = sys.argv[1]
    except IndexError:
        # Except on no args taken; inform user of correct usage
        print('Usage: python3 data-normalizer.py <file>')
        sys.exit(1)

    main(file)