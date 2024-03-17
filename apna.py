# conditiomnal statement
# single line if/ Ternary operator


# variable declaration
# food = input("food ")
# eat = "yes" if food == 'cake' else 'no'
# print(eat)

# statement
# food = input("food : ")
# print("sweat") if food == "sweat" or food == "jilapi" else print("not sweet")

# clever if  statement
# age = int(input("age : "))
# vote = ("no", "yes")[age >= 18]
# print(vote)

# sal = float(input("Enter your salary: "))
# tax = sal * (0.1, 0.2)[sal <= 50000]
# print(tax)


# print(input("name: "))

#
# frist = float(input("enter frist number : "))
# second = float(input("enter second number: "))
# print("avg", (frist + second)/2)

# a = int(input("frist number : "))
# b = int(input("second nunmber : "))
# print(a >= b)

# a = int(input())
# lastdigit = int(repr(a)[-1])
# print(lastdigit)

# a = int(input())
# digit = int(repr(a)[:-2])
# print(digit)

# a = int(input())
# digit = (a % 100) //10
# print(digit)


# num = int(input("Please give me a number: "))
# print(num)
# thou = int((num // 1000))
# print(thou)
# hun = int((num // 100))
# print(hun)
# ten =int((num // 10))
# print(ten)
# one = int((num // 1))
# print(one)

#
# number = int(input())
# a = number // 100
# b = number // 10 % 10
# c = number % 10
# print(a + b + c)
#
# num = int(input())
# next1 = num + 1
# privioues = num - 1
# print('The next number for the number ' + str(num) + ' is ' + str(next1) + '.')
# print('The previous number for the number ' + str(num) + ' is ' + str(privioues) + '.')


#                            lectutr 2

# str = "apna college"
# print(str[5:len(str)])

# a = float(input())
# s=float(a)-int(a)
# print(int(repr(s)[1:]))
# print())/

# Read the numbers b and h like this:
# a = int(input())
# b = int(input())
# print(a*b/2)

# Read an integer:
# a = int(input())
# b = int(input())
# c = int(input())
# print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
# from math import ceil
# a = int(input())
# b = int(input())
# c = int(input())
# print(ceil(a / 2) + ceil(b / 2) + ceil(c / 2))

# b = float(input())
# num = (float(b) - int(b))
# print(repr(num)[1:])
# # print(num[:2])
#
# x = input()
# print(x.split('.')[1][0])

# First digit after decimal point
b = float(input())
num = (float(b) - int(b))
tnum =(num)
# print(tnum)
print(int(repr(tnum)[2:3]))
# a=[[78,55,66,77],
#      [78,65,54,43],
#        [35,34,65,76],
#          [63,78,65,88]]
# for i, row in enumerate (a):
#     for j, item in enumerate (row):
#         print(f"a[{i}][{j}]={item}", end=" ")
#     print()


# a=[[56,987,97,87],
#    [123,456,789,98],
#     [123,456,789,978],
#      [123,456,789,978]]
# for i, row in enumerate(a):
#     for j, item in enumerate(row):
#         print(f"[{i}][{j}]={item}",end=" ")
#     print()
# city=dict()
# city["dhanmondi"]=1209
# city["cantorment"]=8787
# print(city)
# city.update({"Mohamnjhh":1298})
# print(city)

# colors=set()
# colors={'red',"gdfv","fjfb","hbud","fjfgb"}
# print(colors)
# print("red" in colors)
# print("erkjgbigb" in colors)

# def check(n):
#     if n%2 == 0:
#         return (f"the number {n} is and even number.")
# x=[12,232,3,44,55,63,72,85,93]
# y=list(map(check,x))
# print(y)

# question solve 2023
# 1.
# list=((182,178,187,2737,38378,373,383))
# print(list)
# 2.
# d=[181,178,187,182,189,202,201]
# d.reverse()
# print(d)
# d.sort()
# print(d)
# 3.
"""List can store elements of different types, but arrays can store elements only of the same type.
List provides more flexibility as it doesn't require explicit looping, but arrays require explicit looping to print elements

List:

Dynamic size
Dynamic memory allocation
Slower access time
Efficient insertion/deletion
Multidimensionality with irregular structures
Commonly used when size is unknown or changes frequently
Array:

Fixed size
Contiguous memory allocation
Faster access time
Less efficient insertion/deletion, especially in the middle
Multidimensionality with regular structures
Preferred when size is known in advance or fast access is essential"""


# 2.a
# qna={
#     "hi": "Hi! What can i do now?",
#     "do you know me": "You are from daffodil interr national univer ciuty you are currently study 5th semister ",
#     "thanks for your information": "Thanks for your gratitude"
#
# }
# while True:
#     qs=input()
#
#     if(qs=="quite"):
#         break
#     else:
#         print(qna[qs])

# 3.
# def lists_to_dict(keys, values):
#     result_dict = {}
#     for i in range(len(keys)):
#         result_dict[keys[i]] = values[i]
#     return result_dict
# K = [1001, 1002, 1003, 1004, 1005]
# V = ["USA", "Canada", "China", "Japan", "UK"]
# result_dict = lists_to_dict(K, V)
# print(result_dict)

# 2022
# 1
"""Difference between list and tuple in Python
The following is the table about the difference between list and tuple in Python:

List	Tuple
List is a group of comma-separated values within square brackets and square brackets are mandatory.

Eg: i = [10, 20, 30, 40]

Tuple is a group of comma-separated values within parenthesis and parenthesis is optional.

Eg: t = (10, 20, 20, 40)

Insertion and deletion activities are done more efficiently.	The elements can be accessed more easily.
There are numerous built-in methods available.	There are comparatively fewer built-in methods.
List objects are mutable, i.e., once we create a list object, we can perform any changes in that object.

Eg: i[1] = 70

 

Tuple is an immutable object or immutable list, i.e., If the content is fixed and never changes, then we should go for the tuple.

Eg: t[1] = 20

ValueError: tuple object does not support item assignment.

It takes more time for list iteration. It is significantly slower than a tuple.

It takes less time to iterate on a tuple. It is significantly faster than a list.

If the content is not fixed and keeps on changing, then we should go for a list.	If the content is fixed and never changes, then we should go for the tuple.
List objects cannot be used as keys for dictionaries because keys should be hashable and immutable.	Tuple objects can be used as keys for dictionaries because keys should be hashable and mutable"""

# b,
# def list(L):
#     odd_numbers = []
#     even_numbers = []
#     for i in L:
#         if i % 2 == 1:
#             odd_numbers.append(i)
#         else:
#             even_numbers.append(i)
#     print("The list of odd numbers are:", odd_numbers)
#     print("The list of even numbers are:", even_numbers)
# # Example list
# L = [12, 15, 33, 7, 1, 92, 53, 4, 0]
# # Print the original list
# print("The list is:", L)
# # Call the function to process the list
# list(L)

# 2.
# Program to check if a number is prime or not

# num = int(input("Enter a number: "))
# flag = False
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


#
# value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# value2 = [1, 2, 3]
#
# # Using a for loop to iterate through value and print alongside each element of value2
# for item in value:
#     if item == 5:
#         continue  # Skip printing 5
#     print("break")
#     for item2 in value2:
#         print(item, item2)


# def calculate_waiver(semester_fee, cgpa):
#     if cgpa > 3.5:
#         waiver_percent = 20
#     elif 3.0 <= cgpa <= 3.5:
#         waiver_percent = 10
#     else:
#         waiver_percent = 5
#
#     waiver_amount = semester_fee * waiver_percent / 100
#     return waiver_amount
# semester_fee = int(input("Enter amount: "))  # replace with actual semester fee # replace with actual CGPA
# cgpa = float(input("Enter cgpa: "))
# waiver_amount = calculate_waiver(semester_fee, cgpa)
# print(f"The net waiver amount is: {waiver_amount:.2f}")

# Get two lists as input

# Get two lists as input
list1 = [1, 2, 3]
list2 = [4,2, 5]

# Find common elements
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)

# Print the common elements
if common_elements:
    print("The common elements are:", common_elements)
else:
    print("There are no common elements.")
  
