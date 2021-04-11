"""
Randomisation is used to create "random" data. Python uses Mersenne Twister
algorithm that is a Pseudo Random Number Generator. https://en.wikipedia.org/wiki/Mersenne_Twister

to look at python module documentation askpython.com > search random module

Documentation for lists: https://docs.python.org/3.9/tutorial/datastructures.html?highlight=lists
"""
# modules allow you to use the functionality of another code base into your program
# this is usful to keep your code clean and in smaller pieces
# modules allow for team collaboration as one person can create one module and another person another
# kind of like a car assembly line, some people work on the engine, others on electrical etc...
# import random

'''
# *****EXERCISE 1*****
-show how modules work by creating a new project with a main.py and my_module.py
-inside my_module.py type: 
    pi = 3.14
-inside main.py type:
    import my_module
    
    print(my_module.pi)
'''

# random_int = random.randint(1, 10)
#
# # every time this gets run it will be a different number from the range of 1-10
# print(random_int)
#
# # create a random float number 0.0-1.0 excludes 1.0 (0.0000000 - 0.9999999)
# random_float = random.random()
# print(random_float)
#
#
# # ?? how could we create a random float/decimal between 0 and 5
# random_float_range = random.uniform(0, 5)
# print("random_float", random_float * 5)
# print("random float using uniform", random_float_range)
# # use type casting
# print(float(random_int))

'''
*****EXERCISE 1*****
-create a coin toss program that will tell the user heads or tails
-the first letter should be capitalized Heads not heads
-use the number 0 or 1 to represent heads and tails respectively
  0 = Heads
  1 = Tails
'''
# ANSWER
# coin_side = random.randint(0, 1)
# if coin_side == 0:
#     print("Heads")
# else:
#     print("Tails")

# # *****More complex game for heads or tails*****
# user_pick = input("Pick Heads or Tails? ")
# coin_toss = random.randint(0, 1)
# print(coin_toss)
# heads = 0
# tails = 1
#
# print("The computer selected", coin_toss)
# if coin_toss == 0 and user_pick == "Heads":
#     print("You won.")
# elif coin_toss == 1 and user_pick == "Tails":
#     print("You won.")
# else:
#     print("You lost.")

# *****LISTS*****

# storing information that can be accessed later either one by one or together
#
# creating a list of states instead of writing them one at a time:
# state1 = "Alabama"
# state2 = "Virginia"
#
# -the order they are stored is the order you access the data, this list
# is the order each state joined the union

# states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#           "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#           "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#           "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#           "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#           "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#           "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#           "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#           "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # to access a state, 0 index is first item in list, -1 is the last item
# print(states[0])
# # save to a variable
# first_union_state = states[0]
# print("The first state to join the union was", first_union_state, ".")
#
# # change items of list
# states[2] = "Nueva Gerzee"
# print(states)
#
# # add item to list
# print("last item on list before append", states[-1])
# states.append("Joes State")
# print("last item on list after append", states[-1])
#
# # extend list with a list
# states.extend(["renland", "homeland"])
# print("States extended: ", states)
#
# # clear list
# print("clear list", states.clear())

'''
*****EXERCISE 2*****
-pretend you are at a dinner and you and 5 friends are going to put your names in a 
glass. A name will be drawn from the glass and that person will pay the bill for
everyone.
-you can't use the random.choice() function

beginning code:
names_string = input("Enter your friends names and your for the drawing, separating each name with a comma. "
              "ie. Sam, John, Parker ")
names = names_string.split(", ")

Sam, John, Parker, Tom, Jenny, Samantha
'''
# import random

# names_string = input("Enter your friends names and your for the drawing, separating each name with a comma. "
#                     "ie. Sam, John, Parker ")
# names = names_string.split(", ")
# using the choice function
# print(random.choice(names), "will pay the whole bill.")

# names_length = len(names)
# # this will print 6 so we need to subtract 1 from this value
# print(names_length - 1)
#
# random_number = random.randint(0, names_length)
# # print(random_number)
#
# print(names[random_number], "will pay the whole bill.")

# IndexError
# states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#           "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#           "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#           "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#           "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#           "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#           "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#           "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#           "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# total_states = len(states)
# gives 50 but we start counting from 0 so there are 49 indexes total
# print(total_states)
# this replaces total_states with 50, there are only 49
# print(states[total_states])
# to fix it we need to subtract 1 from the total from len
# print(states[total_states - 1])

# Nested Lists
# fruits = ["strawberries", "apples", "nectarines", "cherries"]
# vegetables = ["kale", "celery", "potatoes", "spinach"]
#
# healthy_foods = [fruits, vegetables]
# # prints with double [[ ]]
# print(healthy_foods)
# to access the values
# healthy_foods[N][N]  # where N are the index numbers
# healthy_foods[0][1]  # prints apples

'''
*****EXERCISE 3*****
-create a board game that will mark an X in the location you specify
-the map is a 3 x 3 square
-the program should allow the user to enter a two digit number. This
number will be where the X gets placed
-the example below would be 21 (column 2, row 1)
-use print statements to print the results and types of data you are manipulating

columns-> 1     2     3
row1 = ["😀", "X", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]

starter code:
row1 = ["😀", "😀", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]
map = [row1, row2, row3]
print(map)
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to place the treasure? ")

## Your code goes here

## last line to print
print(f"{row1}\n{row2}\n{row3}") 

'''
# # ANSWER
# row1 = ["😀", "😀", "😀"]
# row2 = ["😀", "😀", "😀"]
# row3 = ["😀", "😀", "😀"]
# map = [row1, row2, row3]
# print(map)
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to place the treasure? ")
# # use below print statements to make sure what you are printing and type to see
# # what type of data you are processing.
# print("position 0", type(position[0]))
# print("position 1", type(position[1]))
# row_position = int(position[0]) - 1
# print("row position", type(row_position))
# column_position = int(position[1]) - 1
# print("column position", type(column_position))
# print(map[row_position][column_position])
# map[column_position][row_position] = "X"
# print(f"{row1}\n{row2}\n{row3}")

'''
*****EXERCISE 4*****
-create a rock paper scissors game
-get ascii art https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
-ask the user to make a choice: 0 for Rock, 1 for Paper, 2 for Scissors
-print what the computer chose
-you will print one of three options: "You lose", "You win", or "You tied"

Starter code:
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
'''
# ANSWER 1
# import random
#
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# user_option = int(input("Select 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# if user_option > 2 or user_option < 0:
#     print("Your number is not within 0 and 2")
#     exit()
#
# choice_list = [rock, paper, scissors]
# user_selection = choice_list[user_option]
# # print("user_selection", user_selection)
# computer_selection = random.choice(choice_list)
# # print("Computer_selection", computer_selection)
#
#
# if user_selection == choice_list[0] and computer_selection == choice_list[1]:
#     print("Computer chose:", choice_list[1])
#     print("You chose", user_selection)
#     print("You lose.")
# elif user_selection == choice_list[1] and computer_selection == choice_list[2]:
#     print("Computer chose:", choice_list[2])
#     print("You chose", user_selection)
#     print("You lose.")
# elif user_selection == choice_list[2] and computer_selection == choice_list[0]:
#     print("Computer chose:", choice_list[0])
#     print("You chose", user_selection)
#     print("You lose.")
# elif user_selection == computer_selection:
#     print("Computer chose:", computer_selection)
#     print("You chose", user_selection)
#     print("You tied")
# else:
#     print("Computer chose:", computer_selection)
#     print("You chose:", user_selection)
#     print("You won.")

# ANSWER 2
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose.")
#     exit()
#
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice == 0 and computer_choice == 2:
#     print("You win.")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose.")
# elif computer_choice > user_choice:
#     print("You lose.")
# elif user_choice > computer_choice:
#     print("You win.")
# elif computer_choice == user_choice:
#     print("It's a tie.")
