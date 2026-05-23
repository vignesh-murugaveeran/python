#++++++++++++ WITHOUT CASTING ANY DATATYPE +++++++++++++++++++++
x = 5
y = 'Hello'
print(x, y)

#Variables do not need to be declared with any particular type
z = 7
z = 10
print(z)


#++++++++++++++ WITH CASTING-DATATYPE +++++++++++++++++++++++++++++
# If you want to specify the data type of a variable
a = str(10)
b = int(7)
c = float(9)
print(a , b , c)

#
d = int(10)
d = str(9807)
d = float(345)
print(d)


#+++++++++++++++ Get the Type +++++++++++++++++++++++++++++++++++++++++++++++++++++
# You can get the data type of a variable with the type() function.
e = 5
y = "type()"
print(type(e))
print(type(y))
