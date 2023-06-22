from sys import argv, exit
import csv
import re

if len(argv) < 3:
    exit("Missing arguments")

if not(re.match(r'.+\.csv$', argv[1])):
    print(argv[1])
    sys.exit("Fisrt argument must be a csv file")

i=0
with open(argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        i+=1 
        try:
            print(row[argv[2]])
        except:
            sys.exit("Column not found")
with open(argv[1], 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([1] * i)

