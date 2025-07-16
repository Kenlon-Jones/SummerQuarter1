import budget

myBudget = budget.BudgetManager(2500)

print("Total Funds: ", myBudget.funds)
 # Add some items to the budget
myBudget.AddBudget("Books", 100)
myBudget.AddBudget("Rent", 800)
myBudget.AddBudget("Car Note", 200)

# Spend some money on items in our budget
myBudget.Spend("Books", 50)
myBudget.Spend("Rent", 800)
myBudget.Spend("Car Note", 200)

# Display the entire budget
myBudget.PrintBudget()