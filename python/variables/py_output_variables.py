print("Python - Output variables...")

"""
Output Variables
The Python print() function is often used to output variables.
In the print() function, you output multiple variables, separated by a comma:
You can also use the + operator to output multiple variables:

Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
For numbers, the + character works as a mathematical operator:

The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

"""
x = "Python is awesome."
print(x)

print("\nprint, mutiple output ")
k = "Python"
i = "is"
j = "awesome"
print(k, i, j) # output multiple variables, separated by a comma

print('\n')
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("\n")
x = 5
y = 10
print(x + y) # the + character works as a mathematical operator:


x = 5
y = "John"
print("\n", x, y)

print("\nPython - Global Vairiables.")
""" 
    -> Variables created outside of a function are know as global variables.
    -> They can be used by anyone, both inside of  functions and outside.
    --> Example 1: Create a variable outside of a function, and use it inside the function
        
"""
print('Example 1: ')
k = "awesome"
def myfunc():
    print('Python is ' + k)
    
myfunc()

""" 
    -> If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
    -> The global variable with the same name will remain as it was, global and with the original value.
    --> Example 2: Create a variable inside a function, with the same name as the global variable
"""

print("\nExample 2: ")
j = "awesome"
def myfunc():
    j = "fantastic"
    print("Python is " + j)

myfunc()
print("Python is " + j)

print("\n")

""" 
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
print("Example 3:  \n If you use the global keyword, the variable belongs to the global scope:")
def myfunc():
    global n 
    n = "fantastic"
    
myfunc()
print("Python is " + n)
    