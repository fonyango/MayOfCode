# --- DAY EIGHT ---
''' 
1. Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''

def divide_by_two(x):
    ''' 
    Determines the number of times one must repeatedly divide a positive integer greater
    than 2 by 2 before getting a value less than 2

    param x: a positive integer greater than 2
    return : number of times x is divided by 2 before getting a value less than 2
    '''
    counter = 0         # initialize a counter
    while x > 2:
        x = x / 2
        counter +=1
    return counter

# test if the function is working
print(divide_by_two(8))
print(divide_by_two(32))
print(divide_by_two(49))
print(divide_by_two(1000))
