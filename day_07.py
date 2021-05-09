# --- DAY SEVEN --- 
''' 
1. Define the following functions as lambdas, and assign them to variables:
(a) Take one parameter; return its square
(b) Take two parameters; return the square root of the sums of their squares
(c) Take any number of parameters; return their average
(d) Take a string parameter; return a string which contains the unique letters in the input string (in any order)
2. Rewrite all these functions as named functions.

'''
# -- using lambda functions
import math    # for calculation of square root

k = lambda x: x*x                           # Calculates the square of x
l = lambda x,y: math.sqrt((x*x + y*y))      # Calculates the square root of the sum of squares of x and y
m = lambda *args: sum(args)/len(args)       # Calculates the average of parameters of any number
n = lambda s: "".join(set(s.lower()))       # returns a string of unique values from an input string

# test if the lambda functions are working
print(k(3))
print(l(5,6))
print(m(3,4,5,6,7))
print(n("Situations"))

# -- using named functions

def square(x):
    ''' 
    Calculates the square of a number
    param x: a number
    return : square of the number
    '''
    return x*x

def square_root(x,y):
    ''' 
    Calculates the square root of the sum of squares of two parameters
    param x,y: two parameters as input
    return : square root of sum of the squares of x and y.
    '''
    return math.sqrt(x*x+y*y)

def averages(*args):
    ''' 
    Calculates the average of any number parameters
    param *args: parameters of any number
    return : average of the input parameters
    '''
    return sum(args)/len(args)

def unique_letters(s):
    ''' 
    Finds a string of unique letters (in any order) of input string
    param s: a string
    return : unique letters (in any order) of input string
    '''
    return "".join(set(s.lower()))

# test if the named functions are working
print(square(4))
print(square_root(4, 5))
print(averages(1,2,3,4,5))
print(unique_letters("independence"))
