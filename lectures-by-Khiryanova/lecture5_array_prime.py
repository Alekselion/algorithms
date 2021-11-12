def invert_array(A:list):
    """ Обращение массива (поворот задом-наперед). """
    N = len(A)
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    return A


def left_shift(A):
    """ Смещение элементов массива влево на 1. """
    N = len(A)
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[-1] = tmp
    return A


def right_shift(A):
    """ Смещение элементов массива вправо на 1. """
    N = len(A)
    tmp = A[-1]
    for k in range(N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp
    return A


def eratosthenes(num):
    """ Генерация простых чисел. """
    arr = [True] * num
    arr[0] = arr[1] = False
    for i in range(2, num):
        if arr[i]:
            for j in range(i*2, num, i):
                arr[j] = False
    return [i for i in range(num) if arr[i]]


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    arr3 = [1, 2, 3, 4, 5]

    print(f"Inversion:\n\tinp {arr1}\n\tout {invert_array(arr1)}")
    print(f"Left shift:\n\tinp {arr2}\n\tout {left_shift(arr2)}")
    print(f"Right shift:\n\tinp {arr3}\n\tout {right_shift(arr3)}")

    n = 50
    print(f"Prime:\n\tinp {n}\n\tout {eratosthenes(n)}")