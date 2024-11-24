from utility import find_solutions
from termcolor import colored


def input_number(message):
    number = input(colored(f"{message}", "yellow"))

    if not number.isnumeric():
        raise TypeError("Invalid coefficient type! Must be a number!")ol

    return float(number)


def main():
    print(colored("Enter coefficients for quadratic equation (ax^2 + bx + c = 0): ", "yellow"))

    a = input_number("a: ")
    b = input_number("b: ")
    c = input_number("c: ")

    result = find_solutions(a, b, c)

    if type(result) is str:
        print(colored(result, "red"))
    elif type(result) is int or float:
        print(colored("Double solution: ", "green") + f"{result}")
    else:
        print(colored("Solutions: ", "green") + f"{result[0]}, {result[1]}")


if __name__ == '__main__':
    main()

