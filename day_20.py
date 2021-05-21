 
# --- DAY TWENTY ---

''' 
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
''' 
# create a list of monthly expenses
expenses = [2200,2350,2600,2130,2190]

# --- 1. In Feb, how many dollars you spent extra compare to January?

extra_expenditure = expenses[1] - expenses[0]
print(extra_expenditure)

# --- 2. Find out your total expense in first quarter (first three months) of the year.

first_quarter_expenses = 0
for expense in range(0,len(expenses)):
    if expense < 3:
        first_quarter_expenses = first_quarter_expenses + expenses[expense]

print(first_quarter_expenses)

# --- 3. Find out if you spent exactly 2000 dollars in any month

if 2000 in expenses:
    print("Yes, I spent exactly 2000 in one of the months")
else:
    print("No, I didn't spend exactly 2000 at any one point")
    
# --- 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)
print(expenses)

''' --- 5. You returned an item that you bought in a month of April and 
got a refund of 200$. Make a correction to your monthly expense list
based on this.
''' 
expenses[3] = expenses[3] - 200
print(expenses)



