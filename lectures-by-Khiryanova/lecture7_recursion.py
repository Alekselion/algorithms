def factorial(n:int):
    """ Расчет факториала числа. """
    assert n >= 0, "Факториал отрицательного числа не определен."
    if n == 0:
        return 1
    return factorial(n-1) * n


def gcd_v1(a, b):
    """ Поиск Наибольшего общего делителя чисел. """
    if a == b:
        return a
    elif a > b:
        return gcd_v1(a-b, b)
    else:
        return gcd_v1(a, b-a)


def gcd_v2(a, b):
    """ Поиск Наибольшего общего делителя чисел. """
    # if b == 0:
    #     return a
    # return gcdV2(b, a%b)
    return a if b == 0 else gcd_v2(b, a%b)
    

def pow_v1(a:float, n:int):
    """ Возведение числа в степень. """
    if n == 0:
        return 1
    else:
        return pow_v1(a, n-1) * a


def pow_v2(a:float, n:int):
    """ Быстрое возведение числа в степень. """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow_v2(a, n-1) * a
    else:
        return pow_v2(a**2, n//2)


if __name__ == "__main":
    n = 5
    print(f"Factorial:\n\tinp {n}\n\tout {factorial(n)}")

    n1, n2 = 100, 68
    print(f"Euclid v1:\n\tinp {n1}, {n2}\n\tout {gcd_v1(n1, n2)}")
    print(f"Euclid v2:\n\tinp {n1}, {n2}\n\tout {gcd_v2(n1, n2)}")

    n1, n2 = 2, 100
    print(f"Power v1:\n\tinp {n1}^{n2}\n\tout {pow_v1(n1, n2)}")
    print(f"Power v2:\n\tinp {n1}^{n2}\n\tout {pow_v2(n1, n2)}")