"""
functions are defined as:
def <function_name>(parameters):
    code...
    code...

# call the function
<function_name>()

example:
def hello_function(name):
    print(f"Hello {name}, from inside function")


hello_function("Rene")

Functions allow us to create a block of code that can be reused elsewhere
"""


# indentation

# def hello_function(name):
#     print(f"Hello {name}, from inside function")
#     print("Inside again.")
#
# # not part of the function
# print("This is outside the functions")
#
# hello_function("Rene")

# PARAMETERS

# positional parameters, have to pass the parameter number or will fail
# TypeError
# def my_parameter_function(qty, item, price):
#     print(f"{qty} {item} costs ${price:.2f}")
#
#
# my_parameter_function(3, "apples")  # this will fail

# parameters with default arguments(keyword arguments)


# def my_parameter_function(qty=3, item="fruits", price=3.00):
#     print(f"{qty} {item} costs ${price:.2f}")


# my_parameter_function(2, 5.00)

# you can't specify a positional after keyword argument
# def my_parameter_function(qty, item="fruits", 3.00):
#     print(f"{qty} {item} costs ${price:.2f}")


# my_parameter_function(2, item="jello", price=2.00)

# # adding unlimited arguments
# def unlimited_args(*args):  # the args can be any name but in documentation *args is used
#     print(f"my tuple of arguments", args[0:])


# unlimited_args("rene", "jose", "john")

# # was not working on Pycharm, run in another interpreter


# def print_list(my_list=[]):
#     my_list.append('###')
#     return my_list


# print_list(['Sam', 'Joe', 'Beth'])
# print_list()
# print_list()

# this list will continue to append the ### and it points the the same memory spot
# def print_list(my_list=[]):
#     my_list.append('###')
#     print(id(my_list))
#     return my_list


# print_list()

# # to change above behavior do the following
# def print_list(my_list=None):
#     if my_list is None:
#         my_list = []
#         my_list.append("###")
#     print(id(my_list))
#     return my_list


# print_list()


'''
# while loop, until the test becomes false
# 
# while this_is_true:
#     code...
# '''
# print("Printing number")
# number = 10
# while number != 0:
#     print(number)
#     number -= 1
#
# print("Printing Digit")
# digit = 5
# while not digit == 0:
#     print(digit)
#     digit -= 1

# # infinite loop, dangers of a while loop if it never gets to false
# name = "John"
# while name is "John":
#     print(name == "John")  # test to see if true
#     print(name)
