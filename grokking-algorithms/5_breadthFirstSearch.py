from collections import deque


def person_is_seller(name):
    """ Check what person is seller.
        Return true if name ends with letter 'm' else false.
    """
    return name[-1] == "m"


def breadthFisrtSearch(graph, name):
    """ Find name of smango seller.
        Return name if found else false.
    """
    search_queue = deque()  # create queue
    search_queue += graph[name]  # add all neighbors
    searched = []
    while search_queue:
        person = search_queue.popleft()  # first person
        if not person in searched:
            if person_is_seller(person):
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    
    name = "you"
    expected = "thom"
    real = breadthFisrtSearch(graph, name)
    verdict = "done" if real == expected else "fail"
    print(f"input: {name}\nexpecthomted: {expected}\noutput: {real}\nverdict: {verdict}")

