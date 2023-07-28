import os
import graphics


def add(n1, n2):
    """Addition"""
    return (n1+n2)
def sub(n1, n2):
    """substraction"""
    return(n1-n2)
def multi(n1, n2):
    """multiplication"""
    return(n1*n2)
def divide(n1, n2):
    """division"""
    return(n1/n2)

on = True

def calculator():
    print(graphics.logo)
    operations = {"+":add, # this is the dictionary, its in this weird position bc variables getting undefined err
                "-":sub,
                "*":multi,
                "/":divide}

    again = True

    #inputs
    n1 = float(input("please enter the first number:- ")) #1st number

    while again:
        for ops in operations: #printing list of operation
            print(ops)
        operation = input("Enter an operation from above:- ")
        n2 = float(input("Enter the next number:- "))# 2nd number

        calc_func = operations[operation] #accessing dictionary for function name
        answer = calc_func(n1, n2) #assigning values to accessed function name

        print(f"{n1}{operation}{n2} = {answer}")
        n1 = answer
        next = input(f"Do you want to continue operation with {n1} type 'y' to continue \n To start a new session press 'n' \n To exit enter any other key :-")
        # continuing with same result as one of the number
        if next == 'y': 
            again = True
            os.system('CLS')
            print(f"Intermediary result:- {answer}")
        # starting calculator again for fresh calculations    
        elif next == 'n':
            os.system('CLS') 
            calculator()   #self call      
        # quitting calculator
        else: 
            again = False
            os.system('CLS')
            print(f"Final result:- {answer}")

calculator()    