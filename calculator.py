# calculator

# multiplication
def multi(x, y):
    z = x * y
    return z


# addition
def add(x, y):
    z = x + y
    return z


# subtraction
def sub(x, y):
    z = x - y
    return z


# division
def div(x, y):
    z = x / y
    return z


while True:
    print("enter two numbers to perform arithmetic operation")
    try:
        a = int(input(" enter first number: "))
        b = int(input(" enter second number: "))
        print("The operations list ('x' -multi, '+' - add, '-' - subs, '/' - div)")
        op = input(" enter the operation you want to perform: ")
        if (op == 'x'):
            c = multi(a, b)
        elif (op == '+'):
            c = add(a, b)
        elif (op == '-'):
            c = sub(a, b)
        elif (op == '/'):
            c = div(a, b)
        else:
            c = "err"  # since not working of any of the above conditions will leave c without any value and that might result in an error
            print(" enter a valid operation")

        print(" Your result is : ", c)
        run = input('To use calculator again enter 1 else enter any other key:')
        if run != '1':
            print('Bye!')
            break
    except:
        print(" you entered an upsupported character")
