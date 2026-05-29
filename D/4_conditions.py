# if - condition
print("if - condition +++++++++++++++++++++++++++++++")
# with number
a = 10
b = 5
if a >= b:
    print("a is greater than b")

# with boolean
isUserLoggedIn = True

if isUserLoggedIn:
    print("Welcome Back!")


# if-elif condition
print("\nif-elif condition +++++++++++++++++++++++++++")
# If the previous conditions were not true, try this elif condition
# Using grade
mark = 73

if mark >= 90:
    print(f"{mark} is Grade A")
elif mark >= 80:
    print(f"{mark} is Grade B")
elif mark >= 70:
    print(f"{mark} is Grade C")
elif mark >= 60:
    print(f"{mark} is Grade D")


# if-elif-else condition
print("\nif-elif-else condition ++++++++++++++++++++++")
# less 0 high
# -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1 0 1, 2, 3, 4, 5, 6, 7, 8

cool = -20

if cool < -20:
    print("It's Cold")
elif cool <= -18:
    print("It's Cool")
else:
    print("Its very Cold")
    
    
print('\nShorthand =====================================')
# Short Hand if
print('Short Hand if ++++++++++++++++++++++++')

# one-line if statement
print('one-line if statement ++++++++++++++')
c = 5
c1 = 7
if c < c1: print('d is greater than c')

# Short Hand If ... Else
print('Short Hand If ... Else +++++++++++++++++++')
e = 67
e1 = 25
print('e1 is greater than e') if e1 > e else print('e is greater than e1')

# Assign a value with if-else
# Ternary operators are particularly useful for simple assignments and return statements.
print('Assign a value with if-else ++++++++++++++++')
f = 13
f1 = 20
bigger = f if f > f1 else f1
print(f'Bigger is {bigger}')


print('one-line three outcome +++++++++++++++++++++')
# one-line three outcome
g = 3457
g1 = 3457
print('g is greater than g1') if g > g1 else print('g and g1 are equal') if g == g1 else print('g is less than g1')


