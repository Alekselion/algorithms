def factorial(num:int):
    """ Return factorial of number. """
    if not isinstance(num, int) or num < 0:
        return False
    
    f = 1
    for i in range(2, num+1):
        f *= i
    return f


if __name__ == "__main__":
    n = 5
    print(f"Fibonacci:\n\tinp {n}\n\tout {factorial(n)}")