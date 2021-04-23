"""
We will use various loops to iterate through various data sets
"""
'''
oses = ["Ubuntu", "Red Hat", "Fedora", "Kali"]

# normally we use a singular of the list but can be anything
for os in oses:
    # these lines are indented and fall inside the for loop.
    # each line will get executed as many times as the loop runs.
    print(os)
    print(os + " Linux")
    print(oses)
print(oses, " from outside the for loop, prints only one time after loop.")
'''
# *****EXERCISE 1*****
'''
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their 
functionality using what you have learned about for loops.
total_height = sum(list)
number_of_students = len(list)
average_height = round(total_height / number_of_students)

Remember to use the round() function to round the average height before you print it.

starter code:
student_heights = input("Input a list of student heights in inches separated by spaces. ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
'''
# # ANSWER
# total_height = 0
#
# student_heights = input("Input a list of student heights in inches separated by spaces. ").split()
# print(student_heights)
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     total_height += student_heights[n]
#     average_height = total_height / len(student_heights)
# print("total_height", total_height)
# print("The average height for students is", round(average_height), "inches.")

# *****EXERCISE 2*****
'''
find the highest number in a list
starter code:
student_scores = input("Input a list of student scores separated by a space\n").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

after writing a for loop use the max() function
'''
# ANSWER

# student_scores = input("Input a list of student scores separated by a space\n").split()
# for i in range(0, len(student_scores)):
#     student_scores[i] = int(student_scores[i])
# print(student_scores)
#
# # highest_score = max(student_scores)
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

'''
Using the range function in a for loop

for number in range(1, 100, 3): # 1=beginning num 100=to num exclusive 3=step 
    print(number)
'''
# for number in range(1, 100):
#     print(number)

# give it a range of numbers and add all the numbers together
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)

# *****EXERCISE 3*****
'''
create a program that will give the sum of all even numbers 1 t0 100 inclusive
'''
# # ANSWER 1
# sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum += number
# print(sum)
#
# # ANSWER 2
# sum2 = 0
# for number in range(2, 101, 2):
#     sum2 += number
# print(sum2)

# *****EXERCISE 4*****
'''
create a program that will print "Fizz" when it encounters a number divisible
by 3. If number is divisible by 5 then print "Buzz". If number is divisible by
both 3 and 5, print "FizzBuzz"
'''
# ANSWER
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# *****FINAL EXERCISE*****
'''
create a random password generator

starter code:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''
# ANSWER
#Password Generator Project
# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level
# password = ""
#
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
#
# print(password)

#Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

