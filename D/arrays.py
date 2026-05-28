# ========================================= List ===============================================
print("LIST******************************************")
a = [121, "cub", [90, "hub"]]
a.append(2)  # It help to add the value in the existing list
a.append("another one")
print(a)
print(len(a))  # It help to find the length in a array
a.remove(121)  # It help to remove the value in the List
a.remove(a[1])
print(a)
print(len(a))

# Using sorted() in List
a = ["10", "2", "30", "4"]

# Sort the list by converting each element to int during comparison
res = sorted(a, key=int)
print(res)

# ======================================== NumPy Array (numpy library) =========================
print("\nNumPy Array******************************************")
"""
NumPy arrays are a part of NumPy library, which is a tool for numerical computing.
Designed for high-performance operations on large datasets and support multi-dimensional arrays 
and matrices, making them suitable for complex mathematical computations.

TO INSTALL THE NUMPY - pip install numpy
"""
import numpy as np

# Element-wise operations
ew = np.array([1, 2, 3, 4])
print(ew * 2)

# Multi-dimensional array
md = np.array([[1, 2], [3, 4]])
print(md * 2)

# ==================================== Array Library (array Library) =======================
print("\nArray Library (array Library)******************************************")
"""
parameter 'i' is the typecode, it tells Python to treat the elements as signed integers ([1, 2, 3])
of a specific byte size (usually 2 or 4 bytes).

Typecode	C Type  	Python Type	    Minimum Size (Bytes)
'b'    	 signed char	    int          	1
'i'	     signed int       	int         	2
'f'	      float	           float         	4
'd'     	double	       float        	8
"""

import array as arr

arrayLib = arr.array("i", [1, 2, 3])  # Try with b, i, f, d
print(arrayLib[0])  # get the first array

# add new element to array
arrayLib.append(7987)
print(arrayLib)


# ================================== FOR LOOP ====================================================
print("\nFOR LOOP******************************************")
# In Dart language
"""
List<int> numbers = [1, 2, 3, 4, 5];

//Loop through values
for (var num  in numbers){
    print(num)
}

//Loop through index
//Based on Index: print 1 \n 2, \n 3, \n......
for (i = 0; numbers.length; i++){
    print('Index no $i, num is ${number[i]}')
}
"""

# import array as arr
arrayLoop = arr.array("i", [3, 4, 5])

# Loop through values
for num in arrayLoop:
    print(num)
    
print("\n")

# Loop through index
for i in range(len(arrayLoop)):
    print(arrayLoop[i], end="  ")

print("\n")

for i in range(0, len(arrayLoop)):
    print(arrayLoop[i], end="  ")


# ================================ ADDING ELEMENT WITH THE insert() ======================================
# Note: We have used *a and *b for unpacking the array elements - Try it then only we can understand
print("\nAdding element using insert(insert-index, new-value)****************************")
insertArray = arr.array("i", [7, 8, 9, 0])
print(*insertArray)

insertArray.insert(1, 876)
print(*insertArray)


# ================================ Accessing the Items using index a[index] =============================
print("\nAccessing the element using index number****************************")
accessIndexArray = arr.array("i", [5, 6, 7, 3])
print(accessIndexArray[2])


# ================================ Removing the elements(.remove() or .pop()) ============================
print("\nUsing .remove() and .pop()********************************")
removeArray = arr.array("i", [5, 3, 5, 2])
# delete the element using number exist in the array(ex: 5)
removeArray.remove(5)
print(removeArray)


# delete the element using index number
removeArray.pop(1)
print(removeArray)


# ================================= SLICING in ARRAY ===============================================
"""
Start at index 3 → value 4
Stop from index 8 → value 9

slicingArray[start index : end index]
slicingArray[3 : 8]
"""

print("\nSLICING in ARRAY******************************************")
sArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slicingArray = arr.array("i", sArray)

res = slicingArray[3:8]
print(*res)


res = slicingArray[6:]
print(*res)

res = slicingArray[:]
print(res)


# ============================== SEARCHING THE ELEMENT ===============================
print("\nSearch the number using .index()****************************************")
# search index number using element([1,2,3,2,1,5])
searchIndex = arr.array("i", [1, 2, 3, 2, 1, 5])

print(f"The number or element 2 found at index {searchIndex.index(2)}")

print(f"The number or element 1 found at index {searchIndex.index(1)}")


# ============================== Updating the element ===============================================
print("\nUpdate the element using the array[index] = 88767 ******************")
updateElement = arr.array("i", [7, 8, 5, 6, 7, 3, 6])

updateElement[3] = 88767
print(updateElement)


# =============================Operations on array ========================================
print("\nOperations on array****************************************")

# ++++++ Counting Elements(value) using .count() +++++++++++++++++
print("Counting Elements(value) using .count()")
countArray = arr.array("i", [3, 4, 5, 3, 7, 3, 5, 7, 5])
count = countArray.count(3)
print(count)


# +++++++ Reversing the elements +++++++++++++++++++++++++
print("Reversing the elements")
reverseArray = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
reverseArray.reverse()
print(*reverseArray)


# +++++++++ Extended elements +++++++++++++++++++++++++++++++++++
print("Extended elements")
extendElement = arr.array("i", [1, 2, 3, 4, 5, 6])
extendElement.extend([4, 9, 8, 7])
print(*extendElement)

# ===================================== append and extend comparison ====================================
print('\nappend and extend comparison******************')
ae = [1, 2]
ae.append([3, 4])
print(ae)
# [1,2,[3,4]]

ae = [1, 2]
ae.extend([3, 4])
print(ae)
# [1,2,3,4]
