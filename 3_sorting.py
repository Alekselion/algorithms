def quick(arr):
    """ Sort arr in ascending order.
        Return a sorted arr.
    """
    if len(arr) < 2:
        return arr
    else:
        item = arr[0]
        less_item = [i for i in arr[1:] if i <= item]
        greater_item = [i for i in arr[1:] if i > item]
        return quick(less_item) + [item] + quick(greater_item)


def merge(arr):
    """ Sort arr in ascending order.
        Return a sorted arr.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge(left)
        merge(right)
        index_left = index_right = index_object = 0

        while index_left < len(left) and index_right < len(right):
            if left[index_left] < right[index_right]:
                arr[index_object] = left[index_left]
                index_left += 1
            else:
                arr[index_object] = right[index_right]
                index_right += 1
            index_object += 1

        while index_left < len(left):
            arr[index_object] = left[index_left]
            index_left += 1
            index_object += 1

        while index_right < len(right):
            arr[index_object] = right[index_right]
            index_right += 1
            index_object += 1

    return arr


def selection(arr):
    """ Sort arr in ascending order.
        Return a sorted arr.
    """
    oldArr = [x for x in arr]
    newArr = []
    for _ in range(len(oldArr)):
        smallest = oldArr[0]
        smallest_idx = 0
        for i in range(1, len(oldArr)):
            if oldArr[i] < smallest:
                smallest = oldArr[i]
                smallest_idx = i
        newArr.append(oldArr.pop(smallest_idx))
    return newArr


def insertion(arr):
    """ Sort arr in ascending order.
        Return a sorted arr.
    """
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert
    return arr


def bubble(arr):
    """ Sort arr in ascending order.
        Return a sorted arr.
    """
    check = True
    while check:
        check = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                check = True
    return arr


if __name__ == "__main__":
    import random
    l = list(range(41))

    random.shuffle(l)
    print(f"Quick:\n\tinp {l}\n\tout {quick(l)}\n")

    random.shuffle(l)
    print(f"Merge:\n\tinp {l}\n\tout {merge(l)}\n")

    random.shuffle(l)
    print(f"Insert:\n\tinp {l}\n\tout {insertion(l)}\n")

    random.shuffle(l)
    print(f"Select:\n\tinp {l}\n\tout {selection(l)}\n")

    random.shuffle(l)
    print(f"Bubble:\n\tinp {l}\n\tout {bubble(l)}\n")