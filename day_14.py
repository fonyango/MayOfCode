# --- DAY FOURTEEN ---

''' 
1. Write a program which sums the integers from 1 to 10 using a for loop (and prints the total at the end).
''' 
sum = 0

for i in range(1,11):
    sum += i

print(sum)

''' 
2. Write a program which finds the factorial of a given number. E.g. 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is
equal to 5 x 4 x 3 x 2 x 1, etc.. Your program should only contain a single loop.
'''
def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i

    return fact

print(factorial(5))
''' 
3. Write a program which prompts the user for 10 floating-point numbers and calculates their sum, product and
average. Your program should only contain a single loop.
'''
# instantiate sum and product
sum = 0
product = 1

# create a loop for the inputs and calculate sum and product
for i in range(0,10):
    x = float(input("Enter a number: "))
    sum += x
    product *= x

# calculate the average
avg = sum/10

# print sum, product and average
print(sum)
print(product)
print(avg)

''' 
4. Rewrite the previous program so that it has two loops – one which collects and stores the numbers, and one
which processes them.
'''
list = [] # instantiate an empty list

# create a list of 10 floating-point numbers
for i in range(0,10):
    num = float(input("Enter a number: "))
    list.append(num)

sum = 0         # instantiate sum
product = 1     # instantiate product 

# compute sum and product
for j in list:
    sum += j
    product *= j

# compute the average
avg = sum/10

# print sum, product and average
print("Sum is ",sum)
print("Product is ",product)
print("Average is ",avg)