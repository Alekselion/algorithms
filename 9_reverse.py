def reverse(arr):
    """ Return inverted iterable object. """
    arr = str(arr)
    if len(arr) == 0:
        return ""

    chars = list(arr)
    for i in range(len(arr) // 2):
        chars[i], chars[len(arr)-i-1] = chars[len(arr)-i-1], chars[i]
    return ''.join(chars)


if __name__ == "__main__":
    s = "hello"
    print(f"Fibonacci:\n\tinp {s}\n\tout {reverse(s)}")