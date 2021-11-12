def gcs(A, B):
    """ Наибольшая общая последовательность.
        Greatest Common Sequence.
    """
    F = [[0] * (len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    
    return F[-1][-1]


def gis(A):
    """ Наибольшая возрастающая последовательность.
        Greatest Increasing Sequence. 
    """
    F = [0] *(len(A) + 1)
    for i in range(1, len(A)+1):
        m = 0
        for j in range(i):
            if A[i-1] > A[j-1] and F[j-1] > m:
                m = F[j-1]
            F[i] = m + 1
    
    return F[len(A)]


if __name__ == "__main__":
    x = [2, 4, 8, 6, 12]
    y = [7, 3, 8, 6, 5]
    print(f"GCS:\n\tinp {x}, {y}\n\tout {gcs(x, y)}")

    x = [2, 4, 1, 6, 12, 31]
    print(f"GIS:\n\tinp {x}\n\tout {gis(x)}")