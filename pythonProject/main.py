# print("hello")
# class Student:
#     print("hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive")
#
# first_student = Student()
# print(f"First student height is {first_student.height}")
# Student.__init__(first_student)

class Student:
    def __init__(self, height = 160):
        self.height = height

nick = Student()
kate = Student(height = 170)
Chiril = Student(height = 2033)
print(nick.height)
print(kate.height)
print(Chiril.height)
print("hello")
