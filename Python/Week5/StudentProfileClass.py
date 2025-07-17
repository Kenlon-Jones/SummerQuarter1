class StudentProfile:

    def __init__(self, name, age, grade, hobbies):
        self.student = {}
        self.student["Name"] = name
        self.student["Age"] = age
        self.student["Grade"] = grade
        self.student["Hobbies"] = hobbies

   
    def SetName(self):
        studentName = input("Enter your student's name: ")
        self.student["Name:"] = studentName

    def SetAge(self):
        studentAge = input("Enter your student's age: ")
        self.student["Age:"] = studentAge

    def SetGrade(self):
        studentGrade = input("Enter your student's grade: ")
        self.student["Grade:"] = studentGrade

    def SetHobbies(self):
        hobbies = []
        hobby = input("Enter your student's hobbies; Type 'done' when done: ").lower()
    

        while hobby != "done":
            hobby = input("Enter your student's hobbies; Type 'done' when done: ").lower()
            hobbies.append(hobby)
            
        self.student["Hobbies"] = hobbies