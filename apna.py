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
