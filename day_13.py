
# --- DAY THIRTEEN ---
''' 
1. Create a list a which contains the first three odd positive integers and a list b which contains the first three even
positive integers.
2. Create a new list c which combines the numbers from both lists (order is unimportant).
3. Create a new list d which is a sorted copy of c, leaving c unchanged.
4. Reverse d in-place.
5. Set the fourth element of c to 42.
6. Append 10 to the end of d.
7. Append 7, 8 and 9 to the end of c.
8. Print the first three elements of c.
9. Print the last element of d without using its length.
10. Print the length of d.
'''
# ---- #1.

''' 
1. Create a list a which contains the first three odd positive integers and a list b which contains the first three even
positive integers.
'''
a = []
b = []
for i in range(1,10):
    if i%2 != 0:
        a.append(i)
        a = a[0:3]
print("List a is {}".format(a))

for j in range(1,10):
    if j%2 == 0:
        b.append(j)
        b = b[0:3]
print("List b is {}".format(b))

''' 
2. Create a new list c which combines the numbers from both lists (order is unimportant).
'''
c = a + b
print("List c is {}".format(c))

''' 
3. Create a new list d which is a sorted copy of c, leaving c unchanged.
'''
d = sorted(c)
print("List d is {}".format(d))

''' 
4. Reverse d in-place.
'''
d = sorted(c, reverse=True)
print("List d reversed is {}".format(d))

''' 
5. Set the fourth element of c to 42.
'''
c.append(42)
print(c)

''' 
6. Append 10 to the end of d.
'''
d.append(10)
print(d)

''' 
7. Append 7, 8 and 9 to the end of c.
'''
c.extend((7,8,9))
print(c)

''' 
8. Print the first three elements of c.
''' 
print(c[0:3])

''' 
9. Print the last element of d without using its length.
'''
print("The last element of d is", d[-1])

''' 
10. Print the length of d.
'''
print("Length of d is {}".format(len(d)))