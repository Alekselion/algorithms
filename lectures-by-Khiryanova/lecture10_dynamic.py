def left_board(A:list, key):
    """ Поиск левой границы для бинарного поиска. """
    A = sorted(A)
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    
    return left


def right_board(A:list, key):
    """ Поиск правой границы для бинарного поиска. """
    A = sorted(A)
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    
    return right


def fib_v1(n):
    """ Генерация серии Фибоначчи рекурсией. """
    if n <= 1:
        return n
    return fib_v1(n-1) + fib_v1(n-2)


def fib_v2(n):
    """ Генерация серии Фибоначчи динамическим 
        программированием. 
    """
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib


def number_trajectories(N):
    """ Вычислить количество способов попасть в
        клетку N, с шагми +1 и +2.
    """
    K = [0, 1] + [0] * (N-1)
    for i in range(2, N+1):
        K[i] = K[i-2] + K[i-1]
    
    return K[N]


def count_trajectories(N, allowed:list):
    """ Вычислить количество способов попасть в
        клетку N, с шагми +1, +2 и +3, при условии, 
        что нельзя попадать в клетки из allowed.
    """
    K = [0, 1, int(allowed[2])] + [0] * (N-2)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]

    return K[N]


def count_min_cost(N, price:list):
    """ Вычислить минимальный способ попасть в
        клетку N, с шагми +1, +2 и +3.
    """
    K = [float("-inf"), price[1], price[1] + price[2]] + [0] * (N-2)
    for i in range(3, N+1):
        K[i] = price[i] + min(K[i-1], K[i-2])

    return K[N]



if __name__ == "__main__":
    arr = [1, 5, 3, 12, 6, 2, 9, 0, 3, 3]
    key = 12
    print(f"Left board:\n\tinp {key}\n\tout {left_board(arr, key)}")
    print(f"Right board:\n\tinp {key}\n\tout {right_board(arr, key)}")

    n = 10
    print(f"Fib v1:\n\tinp {n}\n\tout {fib_v1(n)}")
    print(f"Fib v2:\n\tinp {n}\n\tout {fib_v2(n)}")

    road = 8
    ban = [True] * 3 + [False, True, True, False, True, True]

    print(f"Number traj:\n\tinp {road}\n\tout {number_trajectories(road)}")
    print(f"Count traj:\n\tinp {road}, {ban}\n\tout {count_trajectories(road, ban)}")
    print(f"Min cost:\n\tinp {road}, {ban}\n\tout {count_min_cost(road, ban)}")