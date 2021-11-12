# Brute Force
def linear(arr, item:int):
    """ Find item in arr.
        Return index of item if found else -1.
    """
    if item < min(arr) or len(arr) == 0 or item > max(arr):
        return -1

    for i in arr:
        if i == item:
            return arr.index(i)
    return -1        


if __name__ == "__main__":   
    import random 

    testArray = [x for x in range(1, 11)]
    random.shuffle(testArray)
    number = 7
    expected = testArray.index(number)
    real = linear(testArray, number)
    verdict = "done" if real == expected else "fail"
    
    print(f"input: {number}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")