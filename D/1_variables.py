# (1)
# =============================================== PYTHON VARIABLES ===========================================================
# ++++++++++++ WITHOUT CASTING ANY DATATYPE +++++++++++++++++++++
x = 5
y = "Hello"
print(x, y)

# Variables do not need to be declared with any particular type
z = 7
z = 10
print(z)


# ++++++++++++++ WITH CASTING-DATATYPE +++++++++++++++++++++++++++++
# If you want to specify the data type of a variable
a = str(10)
b = int(7)
c = float(9)
print(a, b, c)

#
d = int(10)
d = str(9807)
d = float(345)
print(d)


# +++++++++++++++ Get the Type +++++++++++++++++++++++++++++++++++++++++++++++++++++
# You can get the data type of a variable with the type() function.
e = 5
y = "type()"
print(type(e), e)
print(type(y), y)


# G will not overwrite g -  Case-Sensitive
g = 4
G = "giant"
print(g, G)


# (2)
# ========================================== PYTHON VARIABLE NAMES ====================================================
# 1
# +++++++++++++++ Legal Variables +++++++++++++++++++++++
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"  # I AM GOING TO USE THIS
MYVAR = "John"
myvar2 = "John"


# ++++++++++++++++ Illegal Variables +++++++++++++++++++++++++++++++++
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# 2
# ++++++++++++++++ Camel Case ++++++++++++++++++++++++++++++++++++++++++
# Each word, except the first, starts with a capital letter:
myVariableName = "John"  # I AM GOING TO USE THIS


# ++++++++++++++++ Pascal Case ++++++++++++++++++++++++++++++++++++++++
# Each word starts with a capital letter:
MyVariableName = "John"


# ++++++++++++++++ Snake Case +++++++++++++++++++++++++++++++++++++++++
# Each word is separated by an underscore character:
my_variable_name = "John"


# (3)
# ================================== Python Variables - Assign Multiple Values ================================

# One value to Multiple Variable
xy = yx = cz = "Blue"
print(xy, yx, cz)

# Multiple Values to Multiple Variable
x, y, z = "Orange", "Red", "Yellow"
print(x, y, z)


# Unpack the Variable
# Python allows you to extract the values into variables. This is called unpacking.
colors = ["grey", "sandle", "light green"]
c, d, e = colors
print(c, d, e)


# (4)
# ================================== Python - Output Variables ================================

x = "Python is hhwb"
print(x)

x = "python"
y = "is"
z = "awesome"
print(x, y, z)

x = "python"
y = "is"
z = "awesome"
print(x + y + z)


x = 7
y = "Hello"
print(x, y)

# We can't plus number with string = it will through error
# x = 7
# y = "Hello"
# print(x + y)

print('Hello', 'World')


# Global Variables
print('Global Variables**********************************')

# Create a variable outside of a function, and use it inside the function
gv = 'fire'

def testing():
    print(f'Print the value from the Global Variables: {gv}')
    
testing()


# Create a variable inside a function, with the same name as the global variable
gv1 = 'awesome'

def testing2():
    gv1 = 'fantastic'
    print(f'Python1 is {gv1}')
    
testing2()

print(f'Python1.1 is {gv1}')


# Global Keyword
print('Global Keyword*********************')

# To create a global variable inside a function, you can use the global keyword.
def testing3():
    global gk
    gk = 'fantastic'

testing3()

print(f'python2 is {gk}')


# use the global keyword if you want to change a global variable inside a function.

gk2 = 'wow'

def testing4():
    global gk2
    gk2 = 'good'
    print(f'python3 is {gk2}')
    
testing4()

print(f'python3.1 is {gk2}')

