def calculate_factorial(n):

    #Returns the factorial of the non-negative integer n.

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)