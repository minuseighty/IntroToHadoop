# Find the monetary value for the highest individual sale for each separate store.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

for line in sys.stdin:
    data = line.strip().split("\t")  # remove whitespace and split on tab
    if len(data) == 6:
        date, time, store, item, cost, payment = data  #assign individual values
        print "{0}\t{1}".format(store, cost)  # print by store and cost
