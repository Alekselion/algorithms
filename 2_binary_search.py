def binary(arr, item):
    """ Find item in arr.
        Return index of item if found else -1.
    """
    if item < min(arr) or len(arr) == 0 or item > max(arr):
        return -1

    arr = sorted(arr)
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    import random 

    testArray = [x for x in range(1, 11)]
    number = 7
    expected = testArray.index(number)
    random.shuffle(testArray)
    real = binary(testArray, number)
    verdict = "done" if real == expected else "fail"
    
    print(f"input: {number}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")