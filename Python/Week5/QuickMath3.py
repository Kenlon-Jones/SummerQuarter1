# 1. Create a class called calculator
# 2. Create a function in the class for each mathematical operation: Addition, Multiplication, Division, Subtraction
# 3. Outside of your class definition, create an instance of your calculator class
# 4. Call each function in your calculator class and store each output into a variable. Use any values for arguments.
# 5. Print all your variables to the console


class Calculator:
    def Add(self, x, y):
        return x + y

    def Subtract(self, x, y):
        return x - y
    
    def Multiply(self, x, y):
        return x * y
    
    def Divide(self, x, y):
        return x / y
    
#Create an object from the calculator class
calculator = Calculator()

sum = calculator.Add(25, 78)
difference = calculator.Subtract(10, 5)
product = calculator.Multiply(5, 8)
divident = calculator.Divide(12, 4)

print(sum)
print(difference)
print(product)
print(divident)