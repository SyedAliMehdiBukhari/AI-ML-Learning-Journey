class Student:
    
    def __init__(self, name, marks):
        self.student_name = name
        self.student_marks = marks
        
    def display_info(self):
        print(f"Student name: {self.student_name}, Student Marks: {self.student_marks}")
        
    def check_result(self):
        if self.student_marks > 40:
            print(f"{self.student_name} is pass with marks {self.student_marks}")
            
        else:
            print(f"{self.student_name} is fail with marks {self.student_marks}")


Ali = Student("Ali", 85)
Hamza = Student("Hamza", 30)

Ali.check_result()
Hamza.check_result()