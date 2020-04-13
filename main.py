# Dennis O'Leary
# Analyzing Monthly Profit and Loss Data

import os
import csv

# input file path
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
months = []
profLoss = []
changes = []

# set initial values
inc = 0
dec = 0
i = 0
j = 0

# open input file, remove header row and loop through the remaining rows to fill the 'months' and 'profLoss' lists
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # add each month to list 'months'
        months.append(row[0])
        # add each Profit/Loss to list 'profLoss'
        profLoss.append(int(row[1]))

# sum of all profit/losses (net profit/loss)
overall = sum(profLoss)
# number of months
numMonths = len(months)
