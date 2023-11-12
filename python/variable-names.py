""" 
  Python Variable Names 
--> A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 

Rules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive 
           # Example;- (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.

"""
# Example 1
"""
print('Legal variable names:')
myvar = "Eric"
my_var = "Eric-spu"
_my_var = "Spu-Eric"
myVar = "eric"
MYVAR = "spu-eric"
myvar2 = "Eric-spu-eric"
print(myVar, my_var, _my_var, myVar, MYVAR, myvar2)

# Example 2
print('Illegal variable names')
2myvar = "eric"
my-var = "eric"
my var = "eric"
"""

""" 
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"
Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"
Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"
"""
# Camel case
myVariableName = "Eric"
print("Camel case:", myVariableName)

# Pascal case
MyVariableName = "Eric-spu"
print("Pascal Case:", myVariableName)

# Snake case
my_variable_name = "Spu-Eric"
print("Snake case:", my_variable_name)