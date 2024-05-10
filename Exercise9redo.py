class Course:
    def Course_data(self,course_code,course_name,credit_hours):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_hours=credit_hours
        print("\nCourse Code :", course_code)
        print("Course Name : ", course_name)
        print("Credit Hours : ", credit_hours)

class CoreCourse(Course):
    def __init__(self,course_code,course_name,credit_hours):
        super().Course_data(course_code,course_name,credit_hours)
    def required(self,required_for_major):
        if required_for_major==1:
            print("\nRequired for major")
        else:
            print("\nNot required for major")

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours,elective_type):
        super().Course_data(course_code,course_name,credit_hours)

        self.elective_type=elective_type
        print("Elective subject is :",elective_type)

code=input("Enter the course code:")
name = input("Enter the course name:")
hours = input("Enter the course time:")
try:
    required=input('\nEnter whether the course is required or not (Yes/No) :')
    corcourse=CoreCourse(code,name,hours)
    if required.lower()=="yes":
        corcourse.required(1)
    elif required.lower()=="no":
        corcourse.required(0)
    else:
        print("\n Enter a valid input.....PLEASE!!")

    elective_type=input(("\nEnter elective subject:"))
    elective_c=ElectiveCourse(code,name,hours,elective_type)
except Exception as error:
    print("An error occured please check",error)







