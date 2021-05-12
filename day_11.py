# --- DAY ELEVEN ---

''' 
An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay.
'''
def employee_weekly_pay(x,y,z):
    '''
    Calculate employee's total weekly pay

    param x: employee's hourly wage
    param y: employee's total regular hours
    param z: employee's total overtime hours
    '''
    overtime_pay = z * 1.5 * x
    total_weekly_pay = x * y + overtime_pay
    return total_weekly_pay

# test if the function works
print(employee_weekly_pay(2785, 40, 21))
print(employee_weekly_pay(4500, 48,15))

