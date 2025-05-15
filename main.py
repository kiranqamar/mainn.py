# Declare class variable before class definition (though it's usually declared inside)
total_students = 0  

class Student:
    # Proper way: class variable declared inside the class
    total_students = 0

    def __init__(self, id, name, class_name):
        self.id = id
        self.name = name
        self.class_name = class_name
        Student.total_students += 1  # Increment class variable

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Class: {self.class_name}"

    def hello(self):
        print("Hello")

    def introduce(self):
        print(f"Hi, I am {self.name} from {self.class_name} class. My ID is {self.id}.")

# Creating 3 student objects
s1 = Student(1, "Ali", "CS4th AI")
s2 = Student(2, "Sara", "CS4th AI")
s3 = Student(3, "Usman", "CS3rd ML")

# Calling introduce() method
s1.introduce()
s2.introduce()
s3.introduce()

# Displaying total number of students
print("Total number of students:", Student.total_students)
