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