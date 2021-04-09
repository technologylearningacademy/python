'''
conditional lesson
if condition:  # if true do
    do this
else:
    do this

< - less than
> - greater than
== - check equality  # = for variables is assignment
<= - less than or equal to
>= - greater than or equal to
!= - not equal to
'''

# Create a flowchart in draw.io for EXERCISE 1

'''
*****EXERCISE 1*****
-prompt a user for a number
-create a program that prints this is an even number for an even number or this is an odd
number for odd numbers
-use the % (modulo) example 7 % 2
'''
# # ANSWER
# num = int(input("Please enter a number to check if it's odd or even: "))
#
# if num % 2 == 0:
#     print("This number is even. ")
# else:
#     print("This number is odd.")


# ###Nested if conditions###
# if condition:  # if true do
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# ask user height in inches and if < 48" can't ride
# ticket prices per age roller coaster <12 $5, 12-18 $7, >18 $12
# height = int(input("What is your height in inches "))
#
# # show difference between ==, !=, <, >
# # set a variable for the total cost
# total = 0
#
# if height > 48:
#     print("You can ride the roller coaster ")
#
#     wants_picture = input("Would you like a picture for $3 cost, Y or N? ")
#
#     if wants_picture == "Y":
#         total += 3
#     age = int(input("What is your age? "))
#     if age < 12:
#         total = 5
#         print(f"Your ticket costs $5.")
#     elif age <= 18:
#         total = 7
#         print(f"Your ticket costs $7")
#     else:
#         print("Your ticket costs $12.")
#     print(f"Your total is ${total}")
# else:
#     print("You are too short to ride the roller coaster.")

'''
*****EXERCISE 1*****
-update the BMI calculator to print out peoples weight categories below.
-take your inputs as floats
-round to the nearest whole number
-output should be "Your BMI <BMINumber> falls in the <category type>."
Obese = 30 or higher
Overweight = 25.0 - 29.9
Normal weight = 18.5 - 24.9
Underweight = under 18.5
'''
# # Answer
# height = float(input("Enter your height in inches: "))
# weight = float(input("Enter your weight: "))
# bmi = round((weight * 703) / height ** 2)
#
# if bmi <= 18.5:  # if fails it will go to next condition
#     print(f"Your BMI {bmi} underweight.")
# elif bmi <= 24.9:
#     print(f"Your BMI {bmi}, falls in the normal weight category.")
# elif bmi < 29.9:
#     print(f"Your BMI {bmi} falls in the overweight category.")
# else:
#     print(f"Your BMI {bmi} is in the obese category")


'''
*****EXERCISE 2*****
-check if year input is a leap year. A leap year has to meet all conditions below
1. year has to be divisible by 4 with no remainder
2. except every year that is evenly divisible by 100
3. unless the year is also evenly divisible by 400

questions to ask
divisible by 4 with no remainder? yes -> is it divisible by 100 no -> is it divisible by 
400 yes > it is a leap year
'''
# # Answer

# year = 2009
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

'''
*****EXERCISE 2*****
Create a pizza ordering system
Pizza and options prices
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for small pizza: $2
Pepperoni for Medium or Large Pizza: $3

Extra cheese on any pizza: $1
print a welcome message
aks user for size of pizza they want: S, M, L
add_pepperoni: Y or N
extra_cheese: Y or N

based on what options the user requests, calculate the total price
'''

# # ANSWER 1
# print("Welcome to Pizza Palace")
# size = input("What size pizza would you like? S, M or L ")
# add_pepperoni = input("Would you like pepperoni? Y or N ")
# extra_cheese = input("Would you like extra cheese? Y or N ")
# total = 0
#
# if size == "S":
#     total += 15
#     if add_pepperoni == "Y":
#         total += 3
#     if extra_cheese == "Y":
#         total += 2
# if size == "M":
#     total = 20
#     if add_pepperoni == "Y":
#         total += 3
#     if extra_cheese == "Y":
#         total += 1
# if size == "L":
#     total = 25
#     if add_pepperoni == "Y":
#         total += 3
#     if extra_cheese == "Y":
#         total += 1
#
# print(f"Your order includes a pizza your total is: {total}")
#
# # ANSWER 2
# # Small Pizza: $15
# # Medium Pizza: $20
# # Large Pizza: $25
# #
# # Pepperoni for small pizza: $2
# # Pepperoni for Medium or Large Pizza: $3
# #
# # Extra cheese on any pizza: $1
#
# print("Welcome to Pizza Palace")
# size = input("What size pizza would you like? S, M or L ")
# add_pepperoni = input("Would you like pepperoni? Y or N ")
# extra_cheese = input("Would you like extra cheese? Y or N ")
#
# total = 0
#
# if size == "S":
#     total += 15
# elif size == "M":
#     total += 20
# else:
#     total += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         total += 2
#     else:
#         total += 3
#
# if extra_cheese == "Y":
#     total += 1
#
# print(f"Your total for the order is {total}")

# ###Logical Operators###
# X and Y  # both X and Y need to be true
# B or C  # only one B or C would need to be true
# not D  # reverses a condition if it's true then it becomes false
#
# # try on the iPython
# X = 12
# X > 15
#
# X > 10 and X < 13
# X < 10 and X < 13
#
# X < 13 or X < 13
#
# not X < 13
#
#
#
# # add and or in the roller coaster exercise for people age 45-55
# height = float(input("Enter your height in inches: "))
#
# total = 0
#
# if height > 48:
#     print("You can ride the roller coaster ")
#
#     age = int(input("What is your age? "))
#
#     if age < 12:
#         total = 5
#         print(f"Your ticket costs $5.")
#     elif age <= 18:
#         total = 7
#         print(f"Your ticket costs $7")
#     elif age >= 45 and age <= 55:
#         print("You can ride the roller coaster on us this week.")
#     else:
#         total = 12
#         print("Your ticket costs $12.")
#
#     wants_picture = input("Would you like a picture for $3 cost, Y or N? ")
#     if wants_picture == "Y":
#         total += 3
#     print(f"Your total is ${total}")
# else:
#     print("You are too short to ride the roller coaster.")

'''
# *****EXERCISE 3*****
create a program that will calculate a love score of two people using their first and
last name.
 It takes two peoples names and checks how many times the letters in the word
 TRUE appear. Then check for the number of times the letters in the word LOVE
 appear. Then combine the 2 digits and that gives you the percentage.
 
example:
 
T  R | J L
R  e | e O
U  n | n V
E  e | n E
     | y
T = 0  L = 0
R = 1  O = 0
U = 0  V = 0
E = 3  E = 3

total compatibility is 33%

You will need to implement the two new functions:
lower()
count()

"Rene".lower()
rene
lower_name = "Rene".lower()
lower_name.count("e")  # this will only search for lower e

interpret the love score:
< 10 and > 90
print "Your score is {score}, you go together like coke and mentos."

>= 40 <=50
print your score is {score}, you are alright together

anything else
print "Your score is {score}."
'''

# print("Welcome to the love calculator")
# partner1 = input("Please enter the first and last name of your partner. ie. Linda Python ").lower()
# partner2 = input("Please enter your first name. ie. John Sample ").lower()
#
# combined_names = partner1 + partner2
# print(combined_names.replace(" ", ""))
#
# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# true_total = t + r + u + e
#
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e = combined_names.count("e")
# love_total = l + o + v + e
#
# love_score = int(str(true_total) + str(love_total))
# # integer_love_score = int(love_score)
#
# if love_score < 10 or love_score > 90:
#     print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <=50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your love score is {love_score}")
# print("""
#     ascii drawings: https://www.asciiart.eu/
#                     https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#                     https://fsymbols.com/text-art/
#                     https://ascii.co.uk/
#     ____________________██████
# _________▓▓▓▓____█████████
# __ Ƹ̵̡Ӝ̵̨̄Ʒ▓▓▓▓▓=▓____▓=▓▓▓▓▓
# __ ▓▓▓_▓▓▓▓░●____●░░▓▓▓▓
# _▓▓▓▓_▓▓▓▓▓░░__░░░░▓▓▓▓
# _ ▓▓▓▓_▓▓▓▓░░♥__♥░░░▓▓▓
# __ ▓▓▓___▓▓░░_____░░░▓▓
# ▓▓▓▓▓____▓░░_____░░▓
# _ ▓▓____ ▒▓▒▓▒___ ████
# _______ ▒▓▒▓▒▓▒_ ██████
# _______▒▓▒▓▒▓▒ ████████
# _____ ▒▓▒▓▒▓▒_██████ ███
# _ ___▒▓▒▓▒▓▒__██████ _███
# _▓▓X▓▓▓▓▓▓▓__██████_ ███
# ▓▓_██████▓▓__██████_ ███
# ▓_███████▓▓__██████_ ███
# _████████▓▓__██████ _███
# _████████▓▓__▓▓▓▓▓▓_▒▒
# _████████▓▓__▓▓▓▓▓▓
# _████████▓▓__▓▓▓▓▓▓
# __████████▓___▓▓▓▓▓▓
# _______▒▒▒▒▒____▓▓▓▓▓▓
# _______▒▒▒▒▒ _____▓▓▓▓▓
# _______▒▒▒▒▒_____ ▓▓▓▓▓
# _______▒▒▒▒▒ _____▓▓▓▓▓
# ________▒▒▒▒______▓▓▓▓▓
# ________█████____█████
# _'▀█║────────────▄▄───────────​─▄──▄_
# ──█║───────▄─▄─█▄▄█║──────▄▄──​█║─█║
# ──█║───▄▄──█║█║█║─▄║▄──▄║█║─█║​█║▄█║
# ──█║──█║─█║█║█║─▀▀──█║─█║█║─█║​─▀─▀
# ──█║▄║█║─█║─▀───────█║▄█║─▀▀
# ──▀▀▀──▀▀────────────▀─█║
# ───────▄▄─▄▄▀▀▄▀▀▄──▀▄▄▀
# ──────███████───▄▀
# ──────▀█████▀▀▄▀
# ────────▀█▀
# """)

'''
# *****EXERCISE 4*****
Create a treasure hunt game based on flowcontrol 3.2 slide
Your start code is this:
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
'''

# # ANSWER
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                        "One red, one yellow and one blue. Which color do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
