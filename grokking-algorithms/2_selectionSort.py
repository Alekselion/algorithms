# Divide And Conquer (decomposition)
def findSmallest(arr):
    """
        Find smallest item.
        Return index of smallest item. 
    """
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx


def selection(arr):
    """ Sort arr in ascending order.
        Return arr.
    """
    lenArr = len(arr)
    oldArr = [arr[e] for e in range(lenArr)]
    newArr = []
    for i in range(lenArr):
        smallest = findSmallest(oldArr)
        newArr.append(oldArr.pop(smallest))
    return newArr


if __name__ == "__main__":
    import random 

    testArray = [x for x in range(-5, 5)]
    expected = [x for x in range(-5, 5)]
    random.shuffle(testArray)
    real = selection(testArray)
    verdict = "done" if real == expected else "fail"
    
    print(f"input: {testArray}\nexpected: {expected}\noutput: {real}\nverdict: {verdict}")