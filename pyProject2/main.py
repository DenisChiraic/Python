def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


operation = {'+': add, '-': sub, '*': mul, '/': div}


def calc():
    num1 = float(input("Enter first number: "))
    for i in operation:
        print(i)
    should_continue = True
    while should_continue:
        operations = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        answer = operation[operations](num1, num2)
        print(f"{num1} {operations} {num2} = {answer}")
        more = input(f"Type 'y' to continue calculating with: {answer} ot type 'n' to a new calculation :")
        if more == 'y':
            num1 = answer
        elif more == 'n':
            should_continue = False
            calc()
        else:
            break


calc()
