# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

for line in sys.stdin:
    data = line.strip().split("\t")  #remove whitespace and split on tab
    if len(data) == 6:
        date, time, store, item, cost, payment = data  # assign values 
        print "{0}\t{1}".format(1, cost)  # print number of items and sales total
