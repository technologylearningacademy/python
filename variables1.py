"""
This program is to show people how to accept input and print it out
Programming follows a principle called DRY (DONT REPEAT YOURSELF).
Variables helps us in this regard.
"""
'''
print("Hello programmer!")
input("What is your favorite hobby?")
print(input("How old are you?"))
'''

### VARIABLES

'''
name = input("What is your name? ")

# the plus sign concatenates multiple objects
print(name + " you are " + input('How old are you? ') + " years old.")

print("Your name has", len(name), "characters")

# Another method to do the above line
print("Your name has", len(input("What is your name (using input inside len)")), "characters")
'''

# variables can change
name = "Tommy"
print(name)

name = "Jose"
print(name)

a = 1
b = a
c = b

print(a)
print(b)
print(c)

# brake down variables and give them names that make sense
# variables one single unit
# numbers in first character not allowed
# don't use function names
# show variable not defined error by using a variable that does not exist or typo of variable

first_name = input("\nWhat is your first name?\n")
last_name = input("What is your last name?\n")
name_length = len(name)
age = input("How old are you?\n")
# convert age into int input is default a string
#age = int(input("How old are you? "))

# use variables as you'd like with f (f-string) and {} will talk in next lesson about f-string
print(f"Hello {first_name} {last_name}, your name is {name_length} characters long"
      f" and you are {age} old.")

"""
*****EXERCISE*****
-create an ec2 instance
-create a program that prompts the users to input the following information, 
make sure you are using a newline after each question:
  instance username
  instance IP address
  users key path
  set a variable named output and print the above information in the below format
  ssh -i <keypath> <username>@<IP address>
"""