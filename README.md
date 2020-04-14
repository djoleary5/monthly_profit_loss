# monthly_profit_loss
Created a Python script for analyzing the financial records of a company.

Using a set of financial data called [budget_data.csv](monthly_profit_loss/Resources/budget_data.csv) which is composed of two columns: `Date` and `Profit/Losses`. 

## Steps Taken
* Created two lists; `months` and `profLoss`, and looped though each row of the dataset adding the month and the Profit/Loss to it's respective list.
* Calculated the number of months in the dataset using the `len(months)` and calculated the net profit/loss over the entire period by adding each month's profit or loss using `len(profLoss)`.
* Looped through each monthly Profit/Loss value and calculate the change from the previous month and add each one to list `changes` then calculated the average monthly change pver the entire period.
* Used another loop to find the greates monthly increase and decrease and the months in which each occured.
* Printed the output in the terminal:

