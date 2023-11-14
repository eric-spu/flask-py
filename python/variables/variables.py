# Variables in Python
""" 
--> Variables are containers for storing data values.
-->  py has no command for declaring a variable  
-->  A variable is created the first time a value is assigned to it

"""

#  Example 1
x = 5
y = "Eric"
print(x, y)

# Example 2
# Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.
x = 5 # x is of type integer (int) type
x = "Mutua" # x is of type string (str) type
print(x)

# if need to specify the data type of a variable, this can be don with CASTING
x = str(3) # x is of type string "3"
y = int(3) # y is of type integer 3
z = float(3) # z is of type float 3.0
print(x, y, z)

"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:
"""
#Example
k = "John"
# is the same as
k = 'John'
print(k)

"""
Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:
"""
a = 4
A = "Sally"
#A will not overwrite a
print(a,  A)