favSnack_list = ["Lays chips", "Peanuts", "Cashews", "Pistachios", "Pretzels"]
favSnack_list.sort()
for snack in favSnack_list:
    print(snack)

Collegetuple = ("UCLA", "UCSF", "Howard", "Xaiver", "USC")
for college in Collegetuple:
    print(college)

carAttributes = { "Brand": "Ford",
                 "Model": "Mustang",
                 "Year": "1969",
                 "Version": "Boss 429",
                 "Engine Type": "V8" }
carAttributes["Color"] = "Black"
for attribute in carAttributes:
    print(carAttributes.get(attribute))

numberGrade = {33, 72, 42, 21, 94}
for grade in numberGrade:
    print(grade)