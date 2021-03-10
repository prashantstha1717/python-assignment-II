# 17. Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Divide by 0 Error"


n1 = int(input("Enter a first number: "))
n2 = int(input("Enter another number: "))
operator = input("Enter a operator: ")
print(calculator(n1, n2, operator))