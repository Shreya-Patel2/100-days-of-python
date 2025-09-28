def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations_dictionary = {"+": add,
                         "-": subtract,
                         "*": multiply,
                         "/": divide, }

first_run = 1
first_number = int(input("What's the first number?:"))
while first_run == 1:
    print("+\n-\n*\n/")
    choice = input("Pick an operation:")
    second_number = int(input("What's the next number?:"))

    answer = operations_dictionary[choice](first_number, second_number)

    print(f"{first_number} {choice} {second_number} = {answer}")

    next_step = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

    if next_step == "y":
        first_number = answer
    else:
        first_number = int(input("What's the first number?:"))
