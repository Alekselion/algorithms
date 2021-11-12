def fibonacci(count):
    """ Return list of Fibonacci series. """
    fib = [1, 1]
    for i in range(2, count + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci:\n\tinp {n}\n\tout {fibonacci(n)}")