# Find the monetary value for the highest individual sale for each separate store.

import sys

highestSale = 0  # initalize the highest sale to 'zero'
oldKey = None  # initalize the first store to 'none'

# It will be in the format key\tval
# Where key is the store name, val is the sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")  # remove whitespace and split on tab
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)  # turn current sale price into a float
    if thisSale > highestSale:
        highestSale = thisSale  # set highest sale to current sale if current sale is greater than previous highest sale for store

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey;
        highestSale = 0  # initalize the highest sale to 'zero' once the store changes

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", highestSale  # print store and biggest sale price
