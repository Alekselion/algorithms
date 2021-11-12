def knapsack(things, capacity:int):
    """ Find expensive things that fit in knapsack.
        Return amount of things in knapsack.
    """
    names, prices, weights = [], [], []
    for n, p, w in things:
        names.append(n)
        prices.append(p)
        weights.append(w)

    result = 0
    while names:
        idx = prices.index(max(prices))  # take most expensive thing
        if weights[idx] <= capacity:
            result += prices[idx]
            capacity -= weights[idx]

        prices.pop(idx)
        weights.pop(idx)
        names.pop(idx)

    return result


def cover_sets(states_needed, stations):
    """ Find stations that cover most territories. 
        Return stations.
    """
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


if __name__ == "__main__":     
    print(f"{'*' * 5} knapsack() {'*' * 5}")
    bag = 4
    things = (("guitar", 1500, 1), ("notebook", 2000, 3), ("record player", 3000, 4))
    expected = 3000
    real = knapsack(things, bag)
    verdict = "done" if real == expected else "fail"
    print(f"input: {things}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    bag = 4
    things = (("guitar", 1500, 1), ("iphone", 2000, 1), ("notebook", 2000, 3), ("record player", 3000, 4))
    expected = 3000
    real = knapsack(things, bag)
    verdict = "done" if real == expected else "fail"
    print(f"\ninput: {things}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

    print(f"\n{'*' * 5} Test cover_sets() {'*' * 5}")
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    print(f"Case 1:\n\tinp {states_needed}\n\t    {stations}\n\tout {cover_sets(states_needed, stations)}")
    