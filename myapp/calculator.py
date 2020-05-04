""" A moduel with a class for unittest demo """

class Calculator():
    """ A class with basic calculator methods for testing """

    def __init__(self):
        pass


    def add(self, num1, num2):
        """ a add method to add two numbers """
        return num1 + num2

    def subtract(self, num1, num2):
        """ a subtract method to subtract two numbers """
        return num1 - num2

    def multiply(self, num1, num2):
        """ a multiply method to multiply two numbers """
        return num1 * num2

    def divide(self, num1,  num2):
        """ a divide method to divide two numbers """
        try:
            result = num1 / num2
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            return result



if __name__ == '__main__':
    cal = Calculator()

    print(cal.add(5, 4))
    print(cal.subtract(4, 6))
    print(cal.multiply(3, 4))
    print(cal.divide(5, 0))