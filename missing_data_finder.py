#!/usr/bin/env python3
"""
A script to identify missing data in a normalized team-data CSV file.
This script does NOT identify matches that are missing all teams in a match.
"""

__author__ = "Aniket Chadalavada"
__version__ = "0.1.0"
__license__ = "CC0-1.0"

import sys

def main(file):
    # Open CSV File for Parsing
    with open(file, 'r') as f:
        data = f.read()[3:]

    # Split CSV File into Rows
    data = data.split('\n')
    # Split into Columns and Remove First Row (Header)
    data = [row.split(',') for row in data][1:]

    # Create Dictionary to Store Counts
    counts = {}
    # Loop Through Rows and Count Matches
    for match in data:
        # Skip Empty Lines
        if match[0] == '':
            continue
        if match[1] not in counts:
            counts[match[1]] = 0
        counts[match[1]] += 1

    # Count Teams with Missing Data in "total_missing"
    total_missing = 0
    # Store Teams Missing From Matches in "missing_teams"
    missing_teams = ""
    # Count Matches with Missing Data in "count"
    count = 0
    # Loop through "counts" and evaluate afformentioned data
    for match in counts:
        if counts[match] < 6:
            total_missing += 6 - counts[match]
            missing_teams += f"Missing {6 - counts[match]} team(s) from Match {match}. "
            count += 1
            # Split Missing Teams into 2x? Rows
            if count % 2 == 0:
                missing_teams += "\n"

    # Concatenate Results and Print
    final = f"- Missing {total_missing} teams from {count} matches.\n{missing_teams[:-1]}"
    print(final)


if __name__ == "__main__":
    # Take args
    try:
        file = sys.argv[1]
    except IndexError:
        # Except on no args taken; inform user of correct usage
        sys.exit("Usage: python3 hole_finder.py <file.csv>")

    main(file)