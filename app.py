# print('krishna')
# print("o-----")
# print(" ||||")
# print('10' *19)

# price=10
# rating=4.9
# name='mosh'
# is_published=False
# print(price,is_published,rating,name)
# full_name='jon smith'
# age_patient=23
# is_new='true'
# name =input('what is your name? ')
# print('Hi '+ name)

# name=input('what is the person name ')
# name2=input('what is your favourite color ')
# print(name+' likes '+name2)
#
# birth_year=input('birth year')
# print(type(birth_year))
# age=2019 - int(birth_year )
# print(type(age))
# print(age)

#
# waight =input('what is your weight in pounds')
# finlly= (0.453592*float(waight))
# print(float(finlly))

# course='''
# hi krishna,
#
# here is our frist email to you.
#
# Thank you,
# The support team
#
# '''
# print(course)

# course='python for beginners'
# another= course[:]
# # print(course[-1])
# # print(course[-2])
# # print(course[-3])
# # print(course[-4])
# # print(course[0:5])
# # print(course[1:])
# # print(course[:5])
# print(another)


# frist='john'
# last='Smith'
# now=frist +' ['+last+'] is a coder'
# msg=f'[{frist}] [{last}] is a coder'
# print(msg,now)

#
# course='python for biginnergs'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('b'))
# print(course.find('biginnergs'))
# print(course.replace('biginnergs','absolute'))
# print(course.replace('p','j'))
# print('python' in course)
# print('Python' in course)


# arithmatic operator
# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)

# assainment operator

# x=90
# x=x+90
# x+=90
# print(x)

# x=10+3*2**2
# print(x)

# x=(2+3)*10-3
# print(x)

# math function
# x=2.9
# print(round(x))

# x=9
# print(abs(-2.9))

# import math
# print(math.ceil(2.9))

import math
from multiprocessing.resource_sharer import stop


# print(math.ceil(2.9))
# print(math.floor(2.9))
# print(math.copysign(-8,-9))
# print(math.fabs(2.4))
# print(math.factorial(9))
# print(math.fmod(2.9,10.89))
#
# x=math.sqrt(15)
# print(x)
# x=math.floor(15.4)
# print(x)
# x=math.floor(15.9)
# print(x)
# x=math.ceil(15.4)
# print(x)

# print(math.ceil(15.9))
# x=math.pow(5,2)
# print(x)
# x=(math.pi)
# print(x)

# print(math.e)
#
#
# import math as m
# # import math as m,n,p anything
# print(math.sqrt(25))
# print(m.sqrt(25))

# from math import sqrt,pow
# print(pow(4,5))
#

# is_hot=False
# is_cold=True
# if is_hot:
#     print("It a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("Its a cold")
#     print('wear warm cloth')
# else:
#     print('its a lovely day')
#
#
# print('Enjoy your day')


# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
#
# print(f"Down Payment: ${down_payment}")

# 2 tai jokhon true ba false hoba sudu tokhon e kaj korba
# has_high_income=True
# has_good_creadit=True
# if has_high_income and has_good_creadit:
#     print('Eligible for loan')
#
#
#
#
#     # jakono akta true hota hoba ba false hota hoba
#     has_high_income = False
#     has_good_creadit = True
#     if has_high_income or has_good_creadit:
#         print('Eligible for loan')
#
# has_good_creadit=True
# has_criminal_record=False
# if has_good_creadit and not has_criminal_record:
#     print('Eligibile for loan')


# temperature=45
# if temperature!=30:
#     print("Its a hot day")
# elif temperature<10:
#     print("its a cold day")
# else:
#     print('Its a neigher hot nor cold')
#

# name="jkjhgyjygjugyyibbtugbukhbkheufygveyfgbyeruvfygbehgvghjvhjvj"
#
# if len(name)<3:
#     print("Name must be at least 3 characters")
#
# elif len(name)>50:
#   print("name must be maximum size of 50 characters")
#
# else:
#     print('name looks good')

#
# weight = int(input('weight'))
# unit = input('(L) or (k)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"you are {converted} kilos")
# #
# else:
#     # jodi 1 ta / slash die thahola float result diba r jodi 2 ta slash die thahola int result diba
#
#     converted = weight//0.45
#
# print(converted)


#  how to use while loops
#

# gusing game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("you win")
#         break
# else:
#    print("you lose")


# car game

# guess = ('start', 'stop')
# while guess == ('start', 'stop'):
#     usert = input('guess a opinion')
#     if usert == 'start':
#         print("car started...ready to go")
#     elif usert == 'stop':
#         print("cat stopped")
#         break
#     else:
#       print("i dont understand")


# command = ""
# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("car is already started")
#         else:
#             started = True
#             print("car started.....")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped")
#         else:
#             started = False
#             print("stopped car")
#     elif command == "help":
#         # print ar moddha 3 bar """"""" semiclone dila miultiple line aksatha kaj kora
#         print("""
#     start-car started
#     stop-stopped car
#      quit- to quite
#      """)
#     elif command == "quite":
#         break
#
#     else:
#         print('sorry ,i dont understand your command')

# for loops in pythyon
# for item in range(5,10,2):
#     print(item)


# prices = [10, 30, 20]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# nasted loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# numbers = [10, ]
# for some in numbers:
#     print('x' * some)

# same

# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ''
#     for count in range(x):
#         output += '*'
#     print(output)

# list sexrcise
#
# names=['jon', 'bob','cot','sot','fot']
# names[0]='jon'
# print(names[2:])
# print(names)


# numbers = [6, 9, 0, 5, 45, 8765, 896, 85, 86598, 77767, 97]
# Max = numbers[0]
# for number in numbers:
#     if number > Max:
#         Max = number
# print(Max)


# 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix[0][1] = 20
# # rint(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

# list method/ list function
# last a kono number add korar jonno

# numbers= [8, 4, 6, 7, 3, 3, 6]
# numbers.append(29)
# print(numbers)

# jakono jaigai inset korar jonno
# numbers= [8, 4, 6, 7, 3, 3, 6]
# numbers.insert(2,8)
# print(numbers)


# list tahak j sonkha ta remove korbo sai sonka ta romove() ar vitora bosata hoba
# numbers = [8, 4, 6, 7, 3, 3, 6]
# numbers.remove(4)
# print(numbers)

# sob cliear korar jonno clear method
# numbers = [8, 4, 6, 7, 3, 3, 6]
# numbers.clear()
# print(numbers)

# last item remove korar jonno pop use korbo
# numbers = [8, 4, 6, 7, 3, 3, 6]
# numbers.()
# print(numbers)

# list thaka kono num koto tomo list a asa kuja bar korar jonno index use kori
# numbers = [8, 4, 6, 7, 3, 3, ]
# print(numbers.index(80))


## list jodi index a number daoa asa sai number jodi thaka ba thaka na true ba false dia bojano hoi
# numbers = [8, 4, 6, 7, 3, 3, ]
# print(3 in numbers)


# # ak number list a koto gulo asa sata bar korar jonno count use korbo
# numbers = [8, 4, 3, 3, 6, 3, 7, 3, 3, ]
# print(numbers.count(3))


# list ar number guloka soto thaka boro ba assanding order kora sajanor jonno sort method use korbo
# numbers = [8, 4, 3, 3, 6, 3, 7, 3, 3, ]
# numbers.sort()
# print(numbers)

# list ar number guloka boro thaka sotro ba dissanding order kora sajanor jonno 1st a sort method than reverse method use korbo
# numbers = [8, 4, 3, 3, 6, 3, 7, 3, 3, ]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# list ar sob gulo copy korar jonno copy method use korbo
# numbers = [8, 4, 3, 3, 6, 3, 7, 3, 3, ]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# same number gulo remove korar jonno
# numbers = [1, 34, 6, 6, 4, 33.4, 5, 4, 4, 6]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)


# Tuples ar moddha amar kono number add, remove,korta parbo na
# numbers = [1, 2, 54]
# numbers[0] = 10
# print(numbers[0])
# print(numbers)

# unpacking
#  ar kaj akta number ka akta letter modddh a store kora

# coordinates = (1, 2, 3)
# x, p, z = coordinates
# print(p)

# dictionaries
# customer = {
#         "name":"john smith",
#         "age": 30,
#         "is_verified": True
# }
# customer["birthday"]="jan 1 2057"
# print(customer["birthday"])

# kichu input nita hoba jamon  3 5 64 3 2 2 3 jakno sonka print korta hoba sagulor spelling
# phone = input("phone: ")
# digits_mapping = {
#     "1": " One",
#     "2": " Two",
#     "3": " Three",
#     "4": " Four",
#
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + ""
# print(output)


# emoji converter:)
# split ar kaj holo sentence ta vag kora space thakla

# messeges = input()
# words = messeges.split(' ')
#
# emojis = {
#     ":)": "\U0001F601",
#     ":(": "\U0001F602"
#
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# function ar kaj holo kichu statement ka akta block moddha rakha
# def greet_user():
#     print('hi there ')
#     print('welcome abored')
#
#
# def tonay_tong():
#     print('helloi')
#     print("jatonu")
#
#
# print("start")
# greet_user()
# print("finish")
# tonay_tong()

# parameter ar kaj block reuse kora
# def greet_user(name):
#     print(f'hi {name} ')
#     print('welcome abored')
#
#
# print("start")
# greet_user("john")
# greet_user("marry")
# print("finish")

# 2nd exercise
# def greet_user(Frist_name,last_name):
#     print(f'hi {Frist_name}  {last_name}!')
#     print('welcome aborted')
#
#
# print("start")
# greet_user("john", "smith")
#
# print("finish")


# key word argumnents
# def greet_user(Frist_name, last_name):
#     print(f'hi {Frist_name}  {last_name}!')
#     print('welcome aborted')
#
#
# print("start")
# # last amar jodi mona kori last name ar jaigai frist name hoba abar fast name ar jaigai last name hoba
# # smith and jon holo positional argument
# # frist name and last name is keyword argument
# greet_user(Frist_name="smith", last_name="jon")
#
# print("finish")


# return statement
# kono number ar square korta hola ba kono value return korar jonno
# def square(number):
#     print(number * number)
#
#
# print(square(3))


# creating a reusable function


# def emojis_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "\U0001F601",
#         ":(": "\U0001F602"
#
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
# message = input('>')
# print(emojis_converter(message))


# Exception

#
# try:
#     age = int(input('Age: '))
#     income = 7000
#     risk = income / age
#     print(age)
# except ValueError:
#     print('Invalid value')
# except ZeroDivisionError:
#     print('Invalid value Age cannot be zero')
# finally:
#     print("mutt print")


#
# (Number
# String          simple
# booleans)
# _______
#
# (Lists          complex
# dictionaries)

# classes
# class point:
#     def move(self):
#         print("Moving point")
#
#     def draw(self):
#         print("Drawing")
#
#
# point1 = point()
# point1.move()
#
#
# point2=point()
# point2.draw()

# ex2
# class point:
#     def move(self):
#         print("Moving point")
#
#     def draw(self):
#         print("Drawing")
#
#
# point1 = point()
# point1.x = 20
# point1.y = 29
# print(point1.y)
# point1.move()
#
# point2 = point()
# point2.x = 234
# print(point2.x)
# point2.draw()

# constructor
# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("Moving point")
#
#     def draw(self):
#         print("Drawing")
#
#
# point = point(20, 30)
# print(point.y)
# print(point.x)


# another example
# class person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, i am {self.name}")
#
#
# tonay = person("tonay")
# tonay.talk()
#
# bob = person("bob")
# bob.talk()


#  inheritance
#
# class Mammal:
#     def walk(self):
#         print("dog is walking")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class cat(Mammal):
#     def leg(self):
#         print("4 leg")
#
#
# dog1 = Dog()
# dog1.bark()
# dog1.walk()
# caat1 = cat()
# caat1.leg()

# Modules

























