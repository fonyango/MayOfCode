
# --- DAY TWENTY THREE ---

''' 
1. You have a list of your favourite marvel super heros.
''' 
heros = ['spider man','thor','hulk','iron man','captain america']

'''
Using this find out,

i. Length of the list
ii. Add 'black panther' at the end of this list
iii. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
iv. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
v. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
''' 
# --- i. Length of the list
print("Length of this list is",len(heros))

# --- ii. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

# --- iii. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

# --- iv. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.

heros[1:3] = ['doctor strange']
print(heros)

# --- v. Sort the heros list in alphabetical order

heros.sort()
print(heros)

''' 
2. Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function
'''
x = int(input("Enter a number: "))
odd_list = []
for i in range(0, x):
    if i%2 != 0:
        odd_list.append(i)
print(odd_list)
