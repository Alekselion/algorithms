def quick_pow(x:float, y:int):
    """ Quick power."""
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 1:
        return quick_pow(x, y-1) * x
    else:
        return quick_pow(x**2, y//2)


if __name__ == "__main__":
    n, p = 2, 10
    print(f"Power:\n\tinp {n}^{p}\n\tout {quick_pow(2, 10)}")