# Data Type of list, tuple, frozenset and set are looks like same

'''
Text Type:                   	str
Numeric Types:              	int, float, complex
Sequence Types:              	list, tuple, range
Mapping Type:	                dict
Set Types:	                    set, frozenset
Boolean Type:	                bool
Binary Types:               	bytes, bytearray, memoryview
None Type:	                    NoneType
'''
print('Text Type:*********************************************')
# String - str
print("String - str +++++++++++++++++++++++++++")
a = "Hello World"
a1 = str("Hello World_1")
print(type(a), a1)


print('Numeric Types:*****************************************')
# Integer - int
print("\nInteger - int +++++++++++++++++++++++++++")
b = 3457
b1 = int(345)  # We can also add the ''
print(type(b), b1)

# Float or Double - float
print("\nFloat or Double - float +++++++++++++++++++++++++++")
c = 42.78
c1 = float(65982)
print(type(c), c1)

# Complex(int(mutiple numbers) + j) - complex
print("\nComplex(int(mutiple numbers) + j) - complex +++++++++++++++++++++++++++++")
d = 8748379j
d1 = complex(89478734j)
print(type(d), d1)


print('Sequence Types:****************************************')
# List - list
print("\nList - list +++++++++++++++++++++++++")
e = ["Hello", "World", 3457]
e1 = list(("Hello", "World", 3457))
print(type(e), e1)

# Tuple - tuple
print("\nTuple - tuple ++++++++++++++++++++++++")
f = ("Hello", "World", 569)
f1 = tuple(("Hello", "World", 78897))
print(type(f), f1)

# Range - range
print("\nRange - range ++++++++++++++++++++++")
g = range(6)
g1 = range(10)
print(type(g), g1, list(g1))


print('Mapping Type:*******************************************')
# Dictionaries - dict
print('\nDictionaries - dict ++++++++++++++++++++++++++++++')
h = {'name': 'VM', 'age': 21}
h1 = dict(name="uhbcuidb", age=21)
print(type(h), h1)


print('Set Types:*********************************')
# Set - set
print('\nSet -set ++++++++++++++++++++++')
i = {'a-le bhai', 'a-m-k'}
i1 = set(('le bhai', 'm-k'))
print(type(i), i1)

# frozenset
print('\nfrozenset ++++++++++++++++++++++++++++++')
j = frozenset({'apple', 'banana', 'cherry'})
j1 = frozenset(('apple', 'banana', 'cherry'))
print(type(j), j1)

print('Boolean Type:****************************************')
# Boolean - bool
print('\nBoolean - bool +++++++++++++++++++++++')
k = False
k1 = bool(67561) # It will give false, when bool(isEmpty)
print(type(k), k1)

print('Binary Types:********************************')
# Bytes - bytes
print('\nBytes - bytes ++++++++++++++++++++++++++')
l = b'String'
l1 = bytes(5)
print(l, l1)

# ByteArray
print('\nByteArray ++++++++++++++++++++++++++++++++++++')
m = bytearray(1)
m1 = bytearray(2)
print(m, m1)

# memoryView
print('\nMemoryView ++++++++++++++++++++')
n = memoryview(bytes(5))
n1 = memoryview(bytes(5))
print(n, n1)
