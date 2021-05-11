# --- DAY 10 ---

'''
1. Write a Python program to assign grades to students at the end of the year. The program must do the following:
(a) Ask for a student number.
(b) Ask for the student’s tutorial mark.
(c) Ask for the student’s test mark.
(d) Calculate whether the student’s average so far is high enough for the student to be permitted to write the
examination. If the average (mean) of the tutorial and test marks is lower than 40%, the student should
automatically get an F grade, and the program should print the grade and exit without performing the
following steps.
(e) Ask for the student’s examination mark.
(f) Calculate the student’s final mark. The tutorial and test marks should count for 25% of the final mark each,
and the final examination should count for the remaining 50%.
(g) Calculate and print the student’s grade, according to the following table:
Weighted final score Final grade
80 <= mark <= 100 A
70 <= mark < 80 B
60 <= mark < 70 C
50 <= mark < 60 D
mark < 50 E
'''
# ---------------------------------------------------------------------------------------------

student_number = input("Enter Student Number: ")                    # input student number
tutorial_mark = float(input("Enter Student's Tutorial Mark: "))     # input tutorial mark    
test_mark = float(input("Enter Student's Test Mark: "))             # input test mark
average_mark = (tutorial_mark + test_mark) / 2                      # calculate average marks

if average_mark < 40:                                           # determine if student will be permitted to do examination
    print("Student Number {0} scored F grade with an average of {1} marks and is not permitted to write the final examination".format(student_number, average_mark))
else:
    examination_mark = float(input("Enter Examination Mark: "))   # input examination marks
    final_mark = (test_mark/100*25) + (tutorial_mark/100*25) + (examination_mark/100*50)  # calculate final marks

    # determine student's final marks and grade
    if final_mark >= 80:
        print("Student Number {0} scored A grade of {1} marks.".format(student_number,final_mark))
    elif (final_mark >= 70 and final_mark < 80):
        print("Student Number {0} scored B grade of {1} marks.".format(student_number, final_mark))
    elif (final_mark >= 60 and final_mark < 70):
        print("Student Number {0} scored C grade of {1} marks.".format(student_number, final_mark))
    elif (final_mark >= 50 and final_mark < 60):
        print("Student Number {0} scored D grade of {1} marks.".format(student_number, final_mark))
    else:
        print("Student Number {0} scored E grade of {1} marks.".format(student_number, final_mark))
    
'''
2. Implement a simple calculator with a menu. Display the following options to the user, prompt for a selection,
and carry out the requested action (e.g. prompt for two numbers and add them). After each operation, return
the user to the menu. Exit the program when the user selects 0. If the user enters a number which is not in the
menu, ignore the input and redisplay the menu. You can assume that the user will enter a valid integer:
-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
'''
# ---------------------------------------------------------------------------------------------------
# display the menu
main_menu = """
-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
"""
print(main_menu)

# select a menu option and perform an arithmetic operation
while True:
    menu = int(input("Choose a menu: "))
    if menu == 0:
        break

    elif menu == 1:
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("The result is {}".format(x + y))

    elif menu == 2:
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("The result is {}".format(x - y))

    elif menu == 3:
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("The result is {}".format(x * y))

    elif menu == 4:
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("The result is {}".format(x / y))
        
    else:
        print("Invalid Selection")
        # display menu back
        print(main_menu)
        