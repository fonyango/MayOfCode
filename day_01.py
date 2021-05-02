# ----- DAY ONE --------
'''
1. Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
def is_multiple(n,m):
 if (m%n==0):
     print('True: {0} is a multiple of {1}'.format(n,m))
 else:
    print('False: {0} is not a multiple of {1}'.format(n,m))

is_multiple(2,4)   

is_multiple(7,8)

'''
2. Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. 
'''

def is_even(k):
    if k%2 == 0:
        print('{} is an Even Number'.format(k))
    else:
        print('{} is an Odd Number'.format(k))

is_even(2)
is_even(35)

'''
3. Write a short Python function that takes a positive integer n and returns
the squares of all the positive integers smaller than n.
'''
def squares_positive(n):
    for i in range(n):
        print(i**2)

squares_positive(8)

# --- Using comprehension syntax

def new_squares_positive(n):
    Squares = [i*i for i in range(n)]
    print('Squares are:',Squares)

new_squares_positive(8)

'''
4. Write a short Python function that takes a positive integer k and returns
a list of the squares of all the positive even integers smaller than k.
'''

def squares_positive_even_integers(k):
    even_squares = []
    for i in range(k):
        if i%2==0:
            even_squares.append(i**2)
        else:
            pass
    print(even_squares)

squares_positive_even_integers(12)

'''
5. Write a short Python function that takes a positive integer k and returns
a dictionary of all positive odd integers smaller than k as keys and squares of 
the positive odd integers smaller than k as values.
'''
def dict_odd_Positive_integers(k):
    odd_dict = {}
    for i in range(k):
        if i%2==1:
            odd_dict[i] = []
            odd_dict[i].append(i**2)
        else:
            pass
    print(odd_dict)

dict_odd_Positive_integers(10)

# --- Using comprehension syntax
def new_dict_odd_positive_integers(k):
    dict_of_odd_integers = {i: i*i for i in range(k) if i%2==1}
    print('Dictionary of squares of Odd integers less than k is:',dict_of_odd_integers)

newdictOfOddPositiveIntegers(10)