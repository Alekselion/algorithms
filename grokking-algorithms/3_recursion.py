def look_for_key(arr, item):
    """ Find item in arr.
        Return true if item found else false.
    """
    if len(arr) == 0:
        return False

    for i in arr:
        if i == item:  # base case
            return True
        elif isinstance(i, list):
            look_for_key(i, item)  # recursion case
    return False


def countdown(i):
    """ Print countdown number.
    """
    print(i, end=' ')
    if i <= 1:
        return
    countdown(i-1)


def custom_factorial(x):
    """ Return factorial of number.
    """
    return 1 if x == 1 else (x * custom_factorial(x-1))


def custom_sum(arr):
    """ Return sum of arr.
    """
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + custom_sum(arr[1:])


def custom_count(arr):
    """Return count of arr.
    """
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    else:
        return 1 + custom_count(arr[1:])


def custom_max(arr):
    """Return maximum item from arr.
    """
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        submax = custom_max(arr[1:])
        return arr[0] if arr[0] > submax else submax


if __name__ == "__main__":     
    print(f"{'*' * 5} Test look_for_key() {'*' * 5}")
    find = "key"
    testArray = [0, 0, [0, [0, [], [find], 0], [], 0], 0, 0]
    expected = True
    real = look_for_key(testArray, find)
    verdict = "done" if real == expected else "fail"
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")
    
    print(f"\n{'*' * 5} Test countdown() {'*' * 5}")
    countdown(5)

    print(f"\n\n{'*' * 5} Test factorial() {'*' * 5}")
    num = 5
    expected = 1 * 2 * 3 * 4 * 5
    real = custom_factorial(num)
    verdict = "done" if real == expected else "fail"
    print(f"input: {num}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test sum() {'*' * 5}")
    testArray = [x for x in range(6)]
    expected = 15
    real = custom_sum(testArray)
    verdict = "done" if real == expected else "fail"
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test count() {'*' * 5}")
    testArray = [x for x in range(6)]
    expected = 6
    real = custom_count(testArray)
    verdict = "done" if real == expected else "fail"
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test max() {'*' * 5}")
    testArray = [x for x in range(6)]
    expected = 5
    real = custom_max(testArray)
    verdict = "done" if real == expected else "fail"
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")