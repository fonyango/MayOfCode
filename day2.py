# ----- DAY TWO -------
'''
1. Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
'''
# import string module
import string

alphabets = list(string.ascii_lowercase) # create a list of all alphabets
print(alphabets)                         # print all the alphabets

'''
2. What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
'''
for i in range(8, -10, -2):      # parameters are start=8, stop=-10, step=-2
    print(i)

'''
3. What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
'''
for k in range(50, 90,10):        # parameters are start=50, stop=90, step=10
    print(k)

'''
4. Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
'''
# --- using list comprehension syntax

powers = [2**i for i in range(9)] # expression followed by a loop
print("Power list is:",powers)

# Alternative Option: ---  using a function without list comprehension, this is how it would look like

def power_integer(k):
    # initialize a power list
    power = []

    #add elements to the power list
    for i in range(k):
        power.append(2**i)  # raise 2 to the power of i and add to the list

    # print power list
    print("List of powers is:", power)

# check using k=9
power_integer(9)

