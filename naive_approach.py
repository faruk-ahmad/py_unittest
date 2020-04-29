import math
import sys

def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2


def test_division_1():
    if division(100, 2) == 50:
        return True
    return False

def test_division_2():
    if division(100, 1) == 100:
        return True
    return False

def test_division_3():
    try:
        division(10, 0)
    except ZeroDivisionError:
        return True
    return False


def test_all():
    error = 0

    if not (test_division_1() and test_division_2() and test_division_3()):
        print(f'Error while dividing')
        error += 1

    if error == 0:
        print(f'No error')
    else:
        print(f'{error}s found')