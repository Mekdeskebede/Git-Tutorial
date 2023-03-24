# This class does arithmetic operations
class ArthimeticClass:
    def add(x, y):
        # adding two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x + y
    def subtract(x, y):
        # subtracting two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x - y
    def multiply(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        
        # multiplying two numbers
        return x * y
    def divide(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")

        if y == 0:
            raise ZeroDivisionError("division by zero")
        
        return x / y