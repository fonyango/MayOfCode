# --- DAY NINE ----

''' 
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
''' 
# -------------------------------------------------------------

# input two numbers x and y
x = float(input('Enter a number: '))
print(x)
operator = input("Choose Operator (+,-,*,/): ")
print("{0} {1}".format(x,operator))
y = float(input('Enter another number: '))
print("{0} {1} {2}".format(x,operator,y))

# perform arithmetic operations based on the chosen operator
if operator == '+':
    print("= {}".format(x + y))
elif operator == '-':
    print("= {}".format(x - y))
elif operator == '*':
    print("= {}".format(x * y))
elif operator == '/':
    print("= {}".format(x/y))
else:
    print("InvalidOperator! Please choose the right operator and try again.")

