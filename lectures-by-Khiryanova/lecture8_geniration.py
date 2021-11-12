def generate_number(N:int, M:int, prefix=None):
    """ Генирирует все чисела (с лидирующими незначащими нулями)
        В N-ричной системе счисления (N <= 10). 
        длины М.
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
        с префиксом prefix.
    """
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)  # * распаковывает
        return
    
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


if __name__ == "__main":
    cc, l = 3, 3
    print(f"Generate number:\n\tinp {cc}, {l}\n\tout {generate_number(cc, l)}")
    print(f"Generate permutations:\n\tinp {l}\n\tout {generate_permutations(l)}")