# --- DAY EIGHT ---
''' 
1. Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''
x = int(input("Enter a positive integer: "))
counter = 0
while x > 2:
    x = x / 2
    counter +=1
print(counter)

