# --- DAY THREE ------
'''
1. Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''

def product_is_odd(values):
    '''
    Checks if there is distinct pairs whose product is odd
    and None when is no distinct pairs whose product is odd

    param values: Sequence of integers
    return: True or None
    '''
    for i in range(len(values)):
        for j in range(len(values)):
            if i!=j:
                product = values[i]*values[j]
                if product%2 != 0:
                    return True
        
v1 = [1,2,4,6,]
v2 = [1,2,3,4,5,6,7]
print(v1, product_is_odd(v1))
print(v2,product_is_odd(v2))

'''
2. Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''
def is_distinct(nums):
    '''
    Checks if there is distinct numbers in the sequence

    param nums: a list of numbers
    return: returns True if there is distinct numbers , else None
    '''

    s = set(nums)       # create a set from the sequence of numbers, nums
    if len(s) == len(nums): # evaluate if the sequence of numbers is equivalent to the set of the numbers
        return True
    else:
        return False

n1 = [1,2,3,6,5,4,8,7,10,8,9]
n2 = [2,4,85,96,144,12,34]

print(n1,is_distinct(n1))
print(n2, is_distinct(n2))

'''
3. Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''
# -- using list comprehension

sequence = [k*(k+1) for k in range(10)]
print(sequence)

# --- Work it out without list conprehension. This is my additional exploration

def new_sequence(k):
    seq = []
    for i in range(k):
        seq.append(i*(i+1))
    print(seq)
        

new_sequence(10)

'''
4. Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
'''
# import random module
import random

def shuffle_int(x,y):
    '''
    Return a random integer using random module
    param (x,y): a sequence of number from x to y
    return : a random number form x to y including both endpoints
    '''
    z = random.randint(x,y)
    print(z)

shuffle_int(1,5)