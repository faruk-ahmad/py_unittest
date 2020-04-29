def addition(num1, num2):
    return num1 + num2

def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2