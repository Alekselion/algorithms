def insert_sort(A):
    """ Сортировка списка А вставками. """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
        
    return A


def choise_sort(A):
    """ Сортировка списка А выбором. """
    N = len(A)
    for pos in range(N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


def bubble_sort(A):
    """ Сортировка списка А методом пузырька. """
    N = len(A)
    for bypass in range(1, N):
        for k in range(N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] =  A[k+1], A[k]
    return A


if __name__ == "__main__":
    arr = [1, 5, 3, 2, 4]
    print(f"Insert:\n\tinp {arr}\n\tout {insert_sort(arr)}")

    arr = [1, 5, 3, 2, 4]
    print(f"Choise:\n\tinp {arr}\n\tout {choise_sort(arr)}")

    arr = [1, 5, 3, 2, 4]
    print(f"Bubble:\n\tinp {arr}\n\tout {bubble_sort(arr)}")