# @Author: Naphat Nithisopa <pection>
# @Date:   2020-12-29T11:43:46+07:00
# @Email:  pection.naphat@gmail.com
# @Last modified by:   pection
# @Last modified time: 2020-12-29T11:43:54+07:00

def my_function():
    print("Hello World")

# Defining our variable
name = "Nicholas"

# Defining a class
class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + ".")
        print("You are studying " + self.course)

class ManageProductCode:
    def __init__(self,filepath):
        self.file_path=filepath
    
