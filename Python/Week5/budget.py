# My task is to convert this program into a class
# 1. Define my class
# 2. Create my __init__() for my class
# 3. Create my instance variable
# 4. Refactor my code into a class

class BudgetManager():
    def __init__(self, amount):

    # The amount of money we have to spend
        self.funds = amount

    # A dictionary of items we are spending on our budget
    # The key is the name of the item; the value is the budget amount for that item
        self.budgets = {}

    # A dicrionary of the exspense of each budgeted item
    # The key is the name of the item; the value is the budget amount for that item
        self.expenses = {}

    # Adds an item to the budgets dictionary
    def AddBudget(self, name, amount):
        if name in self.budgets: # if the key is already in our budgets dictionary
            raise ValueError("Budget for item already exists")
        if amount > funds:
            raise ValueError("No can do, you are too broke")
        self.budgets[name] = amount # Adds the budgeted item to the budgets dictionary
        funds = funds - amount # Subtracts the amount from the funds
        self.expenses[name] = 0 # Add the budgeted item to the expenses dictionary
        return funds

    def Spend(self, name, amount):
        if name not in self.expenses: # if the item is not in our budget
            raise ValueError("Item not in budget")
        self.expenses[name] += amount # Add the expense to the budgeted item
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget           Budgeted         Spent     Remaining")
        print("------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name] # store the amount associated with that key
            spent = self.expenses[name] # store the amount spent on that given tiem
            remainingBudget = budgeted - spent # Calculate the remaining budget for the given 
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} ' 
                f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining = remainingBudget
        print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f} ' 
                f'{totalBudgeted - totalSpent:10.2f}')



    print("Total Funds: ", self.funds)
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