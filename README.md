# monthly_profit_loss
Created a Python script for analyzing the financial records of a company.

## Data
A set of financial data called [budget_data.csv](monthly_profit_loss/Resources/budget_data.csv) which is composed of two columns: `Date` (month-year) and `Profit/Losses` ($). 

## Steps Taken
* Created two lists; `months` and `profLoss`, and looped though each row of the dataset adding the month and the Profit/Loss to it's respective list.
* Calculated the number of months in the dataset using the `len(months)` and calculated the net profit/loss over the entire period by adding each month's profit or loss using `len(profLoss)`.
* Looped through each monthly Profit/Loss value and calculate the change from the previous month and add each one to list `changes` then calculated the average monthly change pver the entire period.
* Used another loop to find the greates monthly increase and decrease and the months in which each occured.
* Printed the output in the terminal:
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
* Created a text file `output.txt` and wrote the output into the file.


