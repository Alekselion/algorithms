def merge(A:list, B:list):
    """ Слияние двух массивов. """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    
    return C


def merge_sort(A):
    """ Сортировка слиянием. """
    if len(A) <= 1:
        return 
    
    middle = len(A) // 2
    left = [A[i] for i in range(middle)]
    right = [A[i] for i in range(middle, len(A))]
    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    for i in range(len(A)):
        A[i] = C[i]
    
    return A


def quick_sort(A):
    """ Быстрая сортировка Тони Хоара. """
    if len(A) <= 1:
        return
    
    barrier = A[0]
    L, M, R = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    
    quick_sort(L)
    quick_sort(R)

    k = 0
    for x in (L + M + R):
        A[k] = x
        k += 1

    return A


if __name__ == "__main__":
    arr = [1, 5, 3, 2, 4]
    print(f"Insert:\n\tinp {arr}\n\tout {merge_sort(arr)}")

    arr = [1, 5, 3, 2, 4]
    print(f"Choise:\n\tinp {arr}\n\tout {quick_sort(arr)}")