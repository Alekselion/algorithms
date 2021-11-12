def divisors(num):
    """ Create list of number divisors.
        Return list.
    """
    return [d for d in range(1, num // 2 + 1) if num % d == 0] + [num]


def triangular(count):
    """ Create list of triangular numbers.
        Rerutn list.
    """
    return [int(t * (t + 1) / 2) for t in range(1, count + 1)]


def pentagonal(count):
    """ Create list of pentagonal numbers.
        Rerutn list.
    """
    return [int(p * (3 * p - 1) / 2) for p in range(1, count + 1)]


def hexagonal(count):
    """ Create list of hexagonal numbers.
        Rerutn list.
    """
    return [int(h * (2 * h - 1) / 2) for h in range(1, count + 1)]


if __name__ == "__main__":
    n1, n2 = 12345, 10
    print(f"Divisors:\n\tinp {n1}\n\tout {divisors(n1)}")
    print(f"Truangular:\n\tinp {n2}\n\tout {triangular(n2)}")
    print(f"Pentagonal:\n\tinp {n2}\n\tout {pentagonal(n2)}")
    print(f"Hexagonal:\n\tinp {n2}\n\tout {hexagonal(n2)}")
