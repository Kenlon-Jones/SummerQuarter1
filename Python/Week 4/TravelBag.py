bedroom = ["Hat", "Shirts", "Shorts", "Shoes", "Charger",]

travelBag = []

print("Pack you bag")
print("Enter the index of an item you'dlike to move from your room to your bag.")
print("Type '100' when you are done packing.\n")
print("Your bedroom items")
for item in bedroom:
    print(item)

item = int(input("Item Index: "))
print(bedroom[item])

while item != 100:
    travelBag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nYour bedroom:")
    print(bedroom)
    print("\nYour travel bag:")
    print(travelBag)
    item = int(input("Item Index: "))

    print("\nYour finished luggage: ")
    for item in travelBag:
        print(item)