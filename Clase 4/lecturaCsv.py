from sys import argv
import sys
import csv
import re

if len(argv) < 3:
    sys.exit("Missing arguments")

if not(re.match(r'.+\.csv$', argv[1])):
    print(argv[1])
    sys.exit("Fisrt argument must be a csv file")

with open(argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            print(row[argv[2]])
        except:
            sys.exit("Column not found")


