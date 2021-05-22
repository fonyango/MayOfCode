# import tkinter module
from tkinter import *

# initialize window manager
window = Tk()

# specify geometry of the window and prevent resising
window.geometry("312x324")
window.resizable(0,0)

# define window title
window.title("Calculator")


def click_button(item):
    ''' 
    continuously update the input field whenever a number is entered 
    or any button is pressed it will act as a button click update.
    '''
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def clear_button():
    ''' 
    clears the input field or previous calculations using the button "C"
    '''
    global expression
    expression = ""
    input_text.set("")


def equals_to_button():
    ''' 
    calculate the expression present in input field. 
    For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5.
    ''' 
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()    # In order to get the instance of the input field 'StringVar()' is used

# structure of the calculator
# create a frame for the input field
input_frame = Frame(window, width=312, height=50, bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

# create an input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial',18,'bold'),textvariable=input_text, width=50, bg='#eee', bd=0, justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

# separate frame which will incorporate all the buttons inside it below the 'input field'
buttons_frame = Frame(window, width=312, height=272.5, bg='grey')
buttons_frame.pack()

# create 'Clear (C)' and 'Divide (/)' buttons on the first row
clear = Button(buttons_frame, text='C', fg='black', width=32, height=3,bd=0, bg='#eee',cursor='hand2', command=lambda:clear_button()).grid(row=0,column=0,columnspan=3, padx=1, pady=1)
divide = Button(buttons_frame, text='/',fg='black',width=10, height=3, bd=0, bg='#eee',cursor='hand2',command=lambda:click_button("/")).grid(row=0,column=3, padx=1, pady=1)

# create buttons '7', '8', '9' and 'Multiply (*)'
seven = Button(buttons_frame, text='7',fg='black', width=10, height=3, bd = 0, bg='#fff', cursor='hand2', command=lambda:click_button(7)).grid(row=1,column=0,padx=1,pady=1)
eight = Button(buttons_frame, text='8', fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(8)).grid(row=1,column=1,padx=1,pady=1)
nine = Button(buttons_frame, text='9',fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(9)).grid(row=1, column=2,padx=1, pady=1)
multiply = Button(buttons_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# create buttons '4', '5', '6' and Subtract (-)'
four = Button(buttons_frame, text='4',fg='black', width=10, height=3, bd = 0, bg='#fff', cursor='hand2', command=lambda:click_button(4)).grid(row=2,column=0,padx=1,pady=1)
five = Button(buttons_frame, text='5', fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(5)).grid(row=2,column=1,padx=1,pady=1)
six = Button(buttons_frame, text='6',fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(6)).grid(row=2, column=2,padx=1, pady=1)
subtract = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor="hand2", command=lambda:click_button("-")).grid(row = 2,column=3, padx = 1, pady = 1)

# create buttons '1', '2', '3' and Addition (+)'
one = Button(buttons_frame, text='1',fg='black', width=10, height=3, bd = 0, bg='#fff', cursor='hand2', command=lambda:click_button(1)).grid(row=3,column=0,padx=1,pady=1)
two = Button(buttons_frame, text='2', fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(2)).grid(row=3,column=1,padx=1,pady=1)
three = Button(buttons_frame, text='3',fg='black', width=10, height=3, bd=0, bg='#fff',cursor='hand2',command=lambda:click_button(3)).grid(row=3, column=2,padx=1, pady=1)
addition = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor="hand2", command=lambda:click_button("+")).grid(row = 3,column=3, padx = 1, pady = 1)

# create buttons '0', '.', '=' 
zero = Button(buttons_frame, text='0',fg='black', width=21, height=3, bd = 0, bg='#fff', cursor='hand2', command=lambda:click_button(0)).grid(row=4,column=0,padx=1,pady=1)
decimal = Button(buttons_frame, text='.', fg='black', width=10, height=3, bd=0, bg='#eee',cursor='hand2',command=lambda:click_button(".")).grid(row=4,column=2,padx=1,pady=1)
equal = Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor="hand2", command=lambda:equals_to_button()).grid(row = 4,column=3, padx = 1, pady = 1)

# display the window until manually closed
window.mainloop()