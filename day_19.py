# ---- DAY NINETEEN ----

class Calculator():
    ''' 
    Simulates a calculator
    '''
    def __init__(self, sales, salaries, transport, taxes):
        self.sales = sales
        self.salaries = salaries
        self.transport = transport
        self.taxes = taxes

    def calculate_expenses(self):
        ''' 
        Calculates the total expenses
        '''
        return (self.salaries + self.transport + self.transport + self.taxes)

    def calculate_profit(self):
        ''' 
        Calculates total profit
        '''
        return (self.sales - (self.salaries + self.transport + self.transport + self.taxes))

    
business1 = Calculator(25548,9658,4510,3203)   # instantiate a class object
print("Total expense is",business1.calculate_expenses())
print("Total profit is",business1.calculate_profit())

    