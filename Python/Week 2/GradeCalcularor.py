# A | Number grade is equal to or greater than 90
# B | Number grade is equal to or greater than 80 and less than 90 
# C | Number grade is equal to or greater than 70 and less than 80
# D | Number grade is equal to or greater than 60 and less than 70
# F | Number grade is less than 60

grade = int(input("Enter your grade number: "))
print(grade)

if grade >= 90:
    print("A")
elif grade >= 80 < 90:
    print("B")
elif grade >= 70 < 80:
    print("C")
elif grade >= 60 < 70:
    print("D")
elif grade < 60:
    print("F")

