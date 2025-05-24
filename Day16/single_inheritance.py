class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
    
class Student(Person):
    def __init__(self, name, id, grade, courses):
        super().__init__(name, id)
        self.grade = grade
        self.courses = courses

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Courses: {self.courses}"
    
student = Student("Samuel", 5678, "B+", ["Math", "Physics", "Computer Science"])
print(student.get_details())