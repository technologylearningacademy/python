# print(len(234)) # errors out so let's understand why

# Data types

# Strings
# sub scripting when you pull out a value or index
print("superman"[0])
print("superman"[-1])

# "12345" is a string not a number
print("12" + "34")

# Integers are all whole numbers
345
print(345 + 321)

# To write large numbers instead of a , we use an underscore. _ gets ignored
print(456_238_768)

# Float, the dot can float around
3.141

# Boolean True or False
print(True)
print(False)

# A function uses a specific entry type and if a wrong entry is used you get a
# type error. Let's try below.
# name_length = (len(input("Enter your name: ")))
# print("Your name has " + name_length + " characters.")

# Like a car it takes gasoline as fuel, if you try and put water it will fail

# Mixing data types gives you errors so we can check what type a data type is with type() function
# type(name_length)

# Type conversion or Type casting. Changing the type of the data
# new_name_length = str(name_length)
# print("Your name has " + new_name_length + " characters.")

num = 345
print(type(num))

num = str(345)
print(type(num))

# What will this print?
print(45 + float("45"))

# What will this print?
print(str(50) + str(100))

# Exercise
'''
-take in a two digit number by using input
-add the two numbers together and print the answer
-for example: 36 would print 9. 23 would print 5
'''
# Answer
# numbers_to_add = input("Please enter a two digit number. \n")
# digit_one = int(numbers_to_add[0])
# digit_two = int(numbers_to_add[1])
# sum = digit_one + digit_two
# print(sum)

# Using Python for Math
# 3 + 6
# 8 - 4
# 2 * 5
# 9 / 3  # returns a float print(type(9 / 3))
# 9 // 3  # returns an integer instead of a float
# 2 ** 3  # exponents
# 6 % 2  # gives remainder of the division

# Operation order PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction)
# ()
# * / # whichever is first in line gets processed first
# + - # whichever is first in line gets processed first

# print(2 + 5 * 2 ** 3)  # what will this return
# print((2 + 5) * 2 ** 3)  # what will this return
# print((2 + 5) * 2 ** 3)  # what will this return
# print((4 + 4) / (5 - 5))  # zero division error

# BMI calculator
# https://www.webmd.com/diet/obesity/qa/what-is-body-mass-index-bmi-and-how-do-you-calculate-it
# BMI = weight(lbs) * 703 / height(inches)
# BMI = kg/m2
# Obese = 30 or higher
# Overweight = 25.0 - 29.9
# Normal weight = 18.5 - 24.9
# Underweight = under 18.5

# height = int(input("Enter your height in inches: "))
# weight = int(input("Enter your weight: "))
# bmi = (weight * 703) / height ** 2
# # bmi_int = int(bmi)  # to remove all numbers past the .
# print(f"Your BMI is {bmi}.")

# Other methods to round and use specific number of decimal values
# print(8 / 3)
# print(round(8 / 3))
# print(round(8 / 3, 2))  # round to N number of places
# print(round(3.58937445, 3))

# Continually operating on a variable
score = 0
score = 1  # same as score = score + 1
# score /= 1
# score *= 1
# score -= 1
# score //= 1
# score **= 1
# print(score)
#
# value = 2
# value **= 4
# print(value)

# f-string
score = 4
name = "James"
isChampion = False

# This will give you type error for trying to add strings to various data objects
# print(name + ", your score is " + score + ". Are you the champion = " + isChampion)

# To fix you could do this but it is too much to write
# print(name + ", your score is " + str(score) + ". Are you the champion = " + str(isChampion))

# f-string to the rescue
print(f"{name} your score is {score}. Are you the champion = {isChampion}")

'''
*****EXERCISE 1*****
-create a calculator that tells you how long you have left to live in days, weeks and years
if you were to live to 80 years old. There are 365 days in one year, 52 weeks in one year.
-ask the user for their current age in years, decide what time you want to use, years weeks, days
-The output should be 
  {person_name} you have {days} days, {weeks} weeks, and {years} years to live.

# ANSWER
person_name = input("Please enter your name: ")
current_age = int(input("Please enter your age in years: "))

years_left = 80 - current_age
days_left = years_left * 365
weeks_left = years_left * 52

print(f"{person_name} you have {days_left} days, {weeks_left} weeks and {years_left} years before you die")


*****EXERCISE 2*****
-create a tip calculator that asks the total check amount (use float type)
-asks what percentage of tip you want to give 10, 15, 20
-asks how many people will split the total bill
-print how much each person should pay (print up to two decimal places only $12.31)

*****Starting information*****
# find percentage of a number
# 15 / 100 = .15
# find the total percentage amount of a total
# $150 * .12 = $18
# add the tip to the bill for total bill
# $150 + 18 = $168
# divide the above total by how many people are splitting the bill
# $168 / 8 = ??? 
'''

bill = float(input("Please enter your total bill: "))
print(f"{bill} bill")

tip_percentage = int(input("What percentage of tip? 10, 15, 20 ")) / 100
print(f"{tip_percentage} tip_percentage")

tip = bill * tip_percentage
print(f"{tip} tip")
total_bill = bill + tip
# print to debug
print(total_bill)
print()
people_splitting = int(input("How many people are splitting the bill? "))
print(f"{people_splitting} people_splitting")
print()
# round if you use an equally divisable number will cause something like 45.0
split_total = round(total_bill / people_splitting, 2)
# to actually print the value to the second decimal place use format
# takes a
split_total2 = "{:.2f}".format(total_bill / people_splitting)
print(f"{split_total} split_total")
print()
print(f"Each person should pay ${split_total}")
print(f"Each person should pay ${split_total2}. This used the :.2f.format option to print")
