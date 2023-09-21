import math
import sympy


def input_int(text):
    do_while = True
    err = False
    while do_while or err:
        do_while = False
        try:
            return int(input(text))
        except ValueError:
            err = True
            print("Invalid input, only accepting numbers!")


operator_list = ["+", "-", "/", "%", "*", "root", "pow"]


def input_operator():
    inp = input("Operator: ")
    if inp not in operator_list:
        print("Invalid input, only accepting operator in the list above!")
        return input_operator()
    else:
        return inp


print("Operator list:")
print(*operator_list, sep=", ")
print("")
num1 = input_int("Operand 1: ")
operand = input_operator()
num2 = input_int("Operand 2: ")


def calc(num1, operand, num2):
    match operand:

        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case "*":
            return num1 * num2
        case "%":
            return num1 % num2
        case "root":
            res = math.pow(num1, 1.0 / num2)
            if num2 == 2:
                return str(sympy.sqrt(num1)) + " or " + str(res)
            return res
        case "pow":
            return math.pow(num1, num2)


print("The result is " + str(calc(num1, operand, num2)))
