# Алгоритм Левенштейна
def levenstein(A, B):
    """ Редакционное расстояние между строками 
    """
    lenA, lenB = len(A), len(B)
    F = [[i+j if i*j == 0 else 0 for j in range(lenB+1)] for i in range(lenA+1)]
    for i in range(1, lenA+1):
        for j in range(1, lenB+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
                
    return F[lenA][lenB]


def equal(A, B):
    """ Равенство строк. """
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


# Алгоритм Кнута-Морриса-Пратта
def search_substring(s, sub):
    for i in range(len(s) - len(sub)):
        if equal(s[i:i+len(sub)], sub):
            return i


if __name__ == "__main__":
    t1, t2 = "колокол", "молоко"
    print(f"Levenstein:\n\tinp {t1}, {t2}\n\tout {levenstein(t1, t2)}")
    
    t1, t2 = "Будем искать подстроку 'ахаха' в этой строке", "ахаха"
    print(f"Search substring:\n\tinp {t1}, {t2}\n\tout {search_substring(t1, t2)}")