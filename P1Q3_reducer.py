import sys

salesTotal = 0  # intialize sales total to 'zero'
transactions = 0  # nitalize number of items sold to 'zero'

for line in sys.stdin:
    data_mapped = line.strip().split("\t")  # remove whitespace and split on tab
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    salesTotal += float(data_mapped[1])  # total sales equals the first element of data added to previous total
    transactions += 1  # transactions total equal previous transaction total 'plus' one

print transactions, "\t", salesTotal  # print transactions and sales totals
