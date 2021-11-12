def gcd(a, b):
    """ Greatest Common Divisor of two numbers. """
    if a == 0 or b == 0:
        return None
    elif a == b:
        return a
    else:
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b


if __name__ == "__main__":
    n1, n2 = 60, 45
    print(f"Euclid:\n\tinp {n1}, {n2}\n\tout {gcd(n1, n2)}")