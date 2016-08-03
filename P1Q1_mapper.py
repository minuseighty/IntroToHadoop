#!/usr/bin/python

# Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

for line in sys.stdin:
    data = line.strip().split("\t")  # get rid of whitespace and split on tab
    if len(data) == 6:
        date, time, store, item, cost, payment = data  # assign individual variables
        print "{0}\t{1}".format(item, cost)  # print item and cost
