# The amount of money we have to spend
funds = 2500

# A dictionary of items we are spending on our budget
# The key is the name of the item; the value is the budget amount for that item
budgets = {}

# A dicrionary of the exspense of each budgeted item
# The key is the name of the item; the value is the budget amount for that item
expenses = {}

# Adds an item to the budgets dictionary
def AddBudget(name, amount):
    global funds
    if name in budgets: # if the key is already in our budgets dictionary
        raise ValueError("Budget for item already exists")
    if amount > funds:
        raise ValueError("No cn do, you are too broke")
    budgets[name] = amount # Adds the budgeted item to the budgets dictionary
    funds = funds - amount # Subtracts the amount from the funds
    expenses[name] = 0 # Add the budgeted item to the expenses dictionary
    return funds

def Spend(name, amount):
    if name not in expenses: # if the item is not in our budget
        raise ValueError("Item not in budget")
    expenses[name] += amount # Add the expense to the budgeted item
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    for name in budgets:
        budgeted = budgets[name] # store the amount associated with that key
        spent = expenses[name] # store the amount spent on that given tiem
        remainingBudget = budgeted - spent # Calculate the remaining budget for the given 
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} ' 
              f'{remainingBudget}')



print("Total Funds: ", funds)
# Add some items to the budget
AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car Note", 200)

# Spend some money on items in our budget
Spend("Books", 50)
Spend("Rent", 800)
Spend("Car Note", 200)

# Display the entire budget
PrintBudget()