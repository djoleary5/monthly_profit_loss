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

# create a list of all changes and calculating the average
while i < (len(profLoss)-1):
    currChg = profLoss[i+1] - profLoss[i]
    changes.append(currChg)
    i = i + 1
avgChg = (sum(changes))/(len(changes))
avgChg = round(avgChg, 2)


# find the greatest profit and loss and capture the index for the month it occurred
while j < (len(changes)):
    if changes[j] > inc:
        inc = changes[j]
        incMon = j + 1
    if changes[j] < dec:
        dec = changes[j] 
        decMon = j + 1
    j = j + 1
    