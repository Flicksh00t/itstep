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

# class Student:
#     def __init__(self, height = 160):
#         self.height = height
#
# nick = Student()
# kate = Student(height = 170)
# Chiril = Student(height = 2033)
# print(nick.height)
# print(kate.height)
# print(Chiril.height)
# print("hello")

# class Student:
#     amount_of_stundents = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_stundents+=1
#
# nick = Student()
# kate = Student(height = 170)
# Chiri = Student()
# print(nick.amount_of_stundents)
# print(Student.amount_of_stundents)
# print(kate.height)

# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
#
# nick = Student()
# kate = Student()


# class Student:
#     height = 160
#
#     def __init__(self):
#         print(self.height)
#         Student.height += 10
#
#
# nick = Student()
# kate = Student()

# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
# nick = Student()
# nick.printer()

# class Locker:
#     print(x)
#     def func_1(self):
#         print(x)
#         def func_2():
#             print(x)
#         func_2()
# some_object = Locker()
# some_object.func_1()

# class Student:
#     amount_of_students = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# print(Student.amount_of_students)
# jora = Student()
# print(Student.amount_of_students)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}"
# nick = Student(name = "Nick")
# print(nick)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}"
#         else:
#             return f"I am a student. I don't have a name"
# alice = Student(name="Alice")
# print(alice)
# unkwown_student = Student()
# print(unkwown_student)

# import random
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#     def to_study(self):
#         print("Este timpul sa invat")
#         self.progress += 0.12
#         self.gladness -= 5
#     def to_sleep(self):
#         print("Voi dormi")
#         self.gladness += 3
#     def to_chill(self):
#         print("Timp pentru odihna")
#         self.gladness += 5
#         self.progress -= 0.1
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("DEAD")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depresie...")
#             self.alive = False
#         elif self.progress > 5:
#             print("O murit de fericire")
#             self.alive = False
#
#
#     def end_of_day(self):
#         print(f"Fericire = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day):
#         day = " Ziua " + str(day) + " din viata lui " + self.name + " "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# tubzik = Student(name="Tudor")
# for day in range(365):
#     if tubzik.alive == False:
#         break
#     tubzik.live(day)

# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passengers(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers != []:
#             print(f"In {self.brand} these are this passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#
#         else:
#             print(f"These are no passengers in {self.brand}")
#
# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Mercedes")
# car.add_passengers(nick)
# car.add_passengers(kate)
# car.print_passengers_names()

# import random
# # Define the House class
# class House:
#     def __init__(self):
#         self.mess = 0
#         self.food = 0
# # Define the Auto class
# class Auto:
#     def __init__(self, brand_list):
#         self.brand = random.choice(list(brand_list))
#         self.fuel = brand_list[self.brand]["fuel"]
#         self.strength = brand_list[self.brand]["strength"]
#         self.consumption = brand_list[self.brand]["consumption"]
#     # Method to simulate driving the car
#     def drive(self):
#         if self.strength > 0 and self.fuel >= self.consumption:
#             self.fuel -= self.consumption
#             self.strength -= 1
#             return True
#         else:
#             print("The car cannot move")
#             return False
# # Define the Job class
# class Job:
#     def __init__(self, job_list):
#         self.job = random.choice(list(job_list))
#         self.salary = job_list[self.job]["salary"]
#         self.gladness_less = job_list[self.job]["gladness_less"]
# # Define the Human class
# class Human:
#     def __init__(self, name="Human", job=None, home=None, car=None):
#         self.name = name
#         self.money = 100
#         self.gladness = 50
#         self.satiety = 50
#         self.job = job
#         self.car = car
#         self.home = home
#     # Method to get a home
#     def get_home(self):
#         self.home = House()
#     # Method to get a car
#     def get_car(self):
#         self.car = Auto(brands_of_car)
#     # Method to get a job
#     def get_job(self):
#         if self.car.drive():
#             self.job = Job(job_list)
#         else:
#             self.to_repair()
#             return
#     def eat(self):
#         if self.home.food <= 0:
#             self.shopping("food")
#         else:
#             if self.satiety >= 100:
#                 self.satiety = 100
#                 return
#             self.satiety += 5
#             self.home.food -= 5
#
#     def work(self):
#         if self.car.drive():
#             self.money += self.job.salary
#             self.gladness -= self.job.gladness_less
#             self.satiety -= 4
#         else:
#             if self.car.fuel < 20:
#                 self.shopping("fuel")
#
#             else:
#                 self.to_repair()
#             return
#     def shopping(self, manage):
#         if self.car.drive():
#             if manage == "fuel":
#                 self.money -= 100
#                 self.car.fuel += 100
#             elif manage == "food":
#                 self.money -= 50
#                 self.home.food += 50
#             elif manage == "delicacies":
#                 self.gladness += 10
#                 self.satiety += 2
#                 self.money -= 15
#
#         else:
#             if self.car.fuel < 20:
#                 manage = "fuel"
#             else:
#                 self.to_repair()
#             return
#
#     def chill(self):
#         self.gladness += 10
#         self.home.mess += 5
#
#     def clean_home(self):
#         self.gladness -= 5
#         self.home.mess = 0
#     def to_repair(self):
#         self.car.strength += 100
#         self.money -= 50
#     def days_indexes(self, day):
#         day = f" Today the {day} of {self.name}'s life "
#         print(f"{day}:=^50")
#         human_indexes = self.name + "'s indexes"
#         print(f"{human_indexes}:^50", "\n")
#         print(f"Money - {self.money}")
#         print(f"Satiety - {self.satiety}")
#         print(f"Gladness - {self.gladness}")
#         home_indexes = "Home indexes"
#         print(f"{home_indexes}:^50", "\n")
#         print(f"Food - {self.home.food}")
#         print(f"Mess - {self.home.mess}")
#         car_indexes = f"{self.car.brand} car indexes"
#         print(f"{car_indexes}:^50", "\n")
#         print(f"Fuel - {self.car.fuel}")
#         print(f"Strength - {self.car.strength}")
#
#     def is_alive(self):
#         if self.gladness < 0:
#             print("Depression...")
#             return False
#         if self.satiety < 0:
#             print("Dead...")
#             return False
#         if self.money < -500:
#             print("Bankrupt...")
#             return False
#         return True

# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except:
#     print("We have an error")
# print("code after capsule")


# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except NameError:
#     print("We have a NameError")
# print("code after capsule")

# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except NameError:
#     print("We have a NameError")
# except ZeroDivisionError:
#     print("We have a ZeroDivisionError")
# print("code after capsule")


# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError):
#     print("We have an error")


# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
# print("code after capsule")

# try:
#     try:
#         print("start code")
#         print(error)
#         print("No errors")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)

# try:
#     print("Hello")
# except:
#     print("We have a problem")
# else:
#     print("No problem")

# try:
#     print("start code")
#     print(error)
#     print("No error")
# except NameError as error:
#     print(error)
# else:
#     print("I am ELSE")
# finally:
#     print("Finally code")

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can't work with {type(var_1)}, " f"we need class str")
#     else:
#         return var_1
#
# first_var = "Hello"
# # first_var = 10
# checker(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "enough material"
#     else:
#         raise BuildingError(amount_of_material)
#
# materials = 123
# check_material(materials, 300)

# import warnings
# warnings.warn("warning no code here", SyntaxWarning)

# # my_list = [1,2,3]
# # iterator = iter(my_list)
# # print(iterator)
# # print(next(iterator))
# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for num in iterator:
#     print(num)
# for num in iterator:
#     print(num)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#
#         return self.i
#
# count = Counter(5)
# # for elem in count:
# #     print(elem)
#
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(iter(count))
# print(next(count))
#
# def numere_pare(maxim):
#     numar = 0
#     while numar < maxim:
#         yield numar
#         numar += 2
#
# for numar in numere_pare(10):
#     print(numar)
#
#
# def generator():
#     yield 1
#     yield 2
#     yield 3
# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for A in range(max_degree):
#         yield number**i
#         i+=1
#
# res = raise_to_the_degrees(122345, 10)
# print(res)
# for A in res:
#     print(A)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards i will help you with {work}"
#
# helper = Helper("homework")
# print(helper("cleaning"))
#
# def helper(work):
#     work_in_memory = work
#     def asd(work):
#         return f"I will help you with your {work_in_memory}. Afterwards i will help you with {work}"
#     return asd
#
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have problems{exc}")
#     else:
#         print(f"No Problems. Result - {result}")
#
# def calculate(expression):
#     return eval(expression)
# checker(calculate, "2+2")
