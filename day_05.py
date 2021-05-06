# -- DAY FIVE ---

'''
1. Write a program which repeatedly prompts the user for an integer. If the integer is even, print the integer. If the
integer is odd, don’t print anything. Exit the program if the user enters the integer 99.
'''
while True:
    x = int(input(" Enter an integer:"))
    if x%2==0:
        print(x)
    elif x==99:
        break

''' 
2. Some programs ask the user to input a variable number of data entries, and finally to enter a specific character
or string (called a sentinel) which signifies that there are no more entries. For example, you could be asked to
enter your PIN followed by a hash (#). The hash is the sentinel which indicates that you have finished entering
your PIN.
Write a program which averages positive integers. Your program should prompt the user to enter integers until
the user enters a negative integer. The negative integer should be discarded, and you should print the average of
all the previously entered integers.
'''

ints = []
while True:
    x = int(input("Enter a positive integer:"))
    avg = 0
    if x > 0:
        ints.append(x)
    else:
        avg = sum(ints)/len(ints)
        print("The input list is {0} and the average is {1}".format(ints,avg))

