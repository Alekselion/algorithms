def knapsack(things:list, capacity:int):
    """ Find expensive things that fit in knapsack.
        Return amount of things in knapsack.
    """
    names, prices, weights = [], [], []
    for count, p, w in things:
        names.append(count)
        prices.append(p)
        weights.append(w)

    count = len(names)

    if count <= 0 or capacity <= 0:
        return 0
    
    cell = [[0 for _ in range(capacity + 1)] for _ in range(count + 1)]
    for i in range(count + 1):
        for j in range(capacity + 1): 
            if i == 0 or j == 0: 
                cell[i][j] = 0
            elif weights[i-1] <= j: 
                cell[i][j] = max(prices[i-1] + cell[i-1][j-weights[i-1]],  cell[i-1][j])
            else: 
                cell[i][j] = cell[i-1][j]

    return cell[-1][-1]


def find_longest_common_substring(txt1:str, txt2:str):
    """ Find longest common substring.
        Return highest value.
    """
    lst1, lst2 = list(txt1), list(txt2)
    cell = [([0]*len(lst2)) for i in range(len(lst1))]
    for x in range(len(lst1)):
        for y in range(len(lst2)):
            if lst1[x] == lst2[y]:
                cell[x][y] = cell[x-1][y-1] + 1
            else:
                cell[x][y] = 0

    return cell[-1][-1]


def find_longest_common_subsequence(txt1:str, txt2:str):
    """ Find longest common subsequence.
        Return highest value.
    """
    lst1, lst2 = list(txt1), list(txt2)
    cell = [([0]*len(lst2)) for i in range(len(lst1))]
    for x in range(len(lst1)):
        for y in range(len(lst2)):
            if lst1[x] == lst2[y]:
                cell[x][y] = cell[x-1][y-1] + 1
            else:
                cell[x][y] = max(cell[x][y-1] , cell[x-1][y])

    return cell[-1][-1]


if __name__ == "__main__":
    print(f"{'*' * 5} knapsack() {'*' * 5}")
    bag = 4
    things = (("guitar", 1500, 1), ("notebook", 2000, 3), ("record player", 3000, 4))
    expected = 3500
    real = knapsack(things, bag)
    verdict = "done" if real == expected else "fail"
    print(f"input: {things}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    bag = 4
    things = (("guitar", 1500, 1), ("iphone", 2000, 1), ("notebook", 2000, 3), ("record player", 3000, 4))
    expected = 4000
    real = knapsack(things, bag)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {things}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test find_longest_common_substring() {'*' * 5}")
    s1, s2 = "hish", "fish"
    expected = 3
    real = find_longest_common_substring(s1, s2)
    verdict = "done" if real == expected else "fail"
    print(f"input: {s1}, {s2}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")
    
    s1, s2 = "hish", "vista"
    expected = 0
    real = find_longest_common_substring(s1, s2)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {s1}, {s2}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test find_longest_common_subsequence() {'*' * 5}")
    s1, s2 = "fosh", "fort"
    expected = 2
    real = find_longest_common_subsequence(s1, s2)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {s1}, {s2}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    s1, s2 = "fosh", "fish"
    expected = 3
    real = find_longest_common_subsequence(s1, s2)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {s1}, {s2}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    s1, s2 = "blue", "clues"
    expected = 3
    real = find_longest_common_subsequence(s1, s2)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {s1}, {s2}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")