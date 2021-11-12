# Divide And Conquer (decomposition)
def quick(arr):
    """ Sort arr in ascending order.
        Return arr.
    """
    if len(arr) < 2:
        return arr
    else:
        item = arr[0]
        less_item = [i for i in arr[1:] if i <= item]
        greater_item = [i for i in arr[1:] if i > item]
        return quick(less_item) + [item] + quick(greater_item)


if __name__ == "__main__":
    import random 

    testArray = [x for x in range(-5, 5)]
    expected = [x for x in range(-5, 5)]
    random.shuffle(testArray)
    real = quick(testArray)
    verdict = "done" if real == expected else "fail"
    
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")