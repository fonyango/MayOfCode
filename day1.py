# ----- DAY ONE --------
'''
1. Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
def isMultiple(n,m):
 if (m%n==0):
     print('True: {0} is a multiple of {1}'.format(n,m))
 else:
    print('False: {0} is not a multiple of {1}'.format(n,m))

isMultiple(2,4)   

isMultiple(7,8)

'''
2. Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. 
'''

def isEven(k):
    if k%2 == 0:
        print('{} is an Even Number'.format(k))
    else:
        print('{} is an Odd Number'.format(k))

isEven(2)
isEven(35)

'''
3. Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''
def sumOfSquaresPositiveIntegers(n):
    for i in range(n):
        print(i**2)

sumOfSquaresPositiveIntegers(8)

# --- Using comprehension syntax

def newsumOfSquaresPositiveIntegers(n):
    sumOfSquares = [i*i for i in range(n)]
    print('Sum of squares is:',sumOfSquares)

newsumOfSquaresPositiveIntegers(8)

'''
4. Write a short Python function that takes a positive integer k and returns
a list of the sum of the squares of all the positive even integers smaller than k.
'''

def sumOfSquaresOfPositiveEvenIntegers(k):
    even_squares = []
    for i in range(k):
        if i%2==0:
            even_squares.append(i**2)
        else:
            pass
    print(even_squares)

sumOfSquaresOfPositiveEvenIntegers(12)

'''
5. Write a short Python function that takes a positive integer k and returns
a dictionary of all positive odd integers smaller than k as keys and sum of the squares of 
all the positive odd integers smaller than k as values.
'''
def dictOfOddPositiveIntegers(k):
    odd_dict = {}
    for i in range(k):
        if i%2==1:
            odd_dict[i] = []
            odd_dict[i].append(i**2)
        else:
            pass
    print(odd_dict)

dictOfOddPositiveIntegers(10)

# --- Using comprehension syntax
def newdictOfOddPositiveIntegers(k):
    dict_of_odd_integers = {i: i*i for i in range(k) if i%2==1}
    print('Dictionary of squares of Odd integers less than k is:',dict_of_odd_integers)

newdictOfOddPositiveIntegers(10)

