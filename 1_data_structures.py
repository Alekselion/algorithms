arr = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8]
]

hash_fun = {
    "apple":0.67, 
    "milk":1.49, 
    "avocado":1.49
}

graph = {
    "a":["b", "c", "d"],
    "b":["e", "f"],
    "c":["e"],
    "d":[],
    "e":[],
    "f":[]
}

# sets
fruites = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])
print(f"Union: {fruites | vegetables}")
print(f"Intersection: {fruites & vegetables}")
print(f"Difference: {fruites - vegetables}")
print(f"Symetric difference: {fruites ^ vegetables}")


class Stack:
    """ Last In First Out"""
    def __init__(self):
        self.stack = []

    def is_empty(self): 
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return "Stack is empty." if self.is_empty(self.stack) else self.stack.pop()
    
    def clear(self):
        self.stack = []
    
    def top(self):
        return "Stack is empty." if self.is_empty(self.stack) else self.stack[-1]


class Queue:
    """ First In First Out"""
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return "Queue is empty." if self.is_empty(self.queue) else self.queue.pop(0)
    
    def clear(self):
        self.queue = []

    def front(self):
        return "Stack is empty." if self.is_empty(self.queue) else self.queue[-1]

    def real(self):
        return "Stack is empty." if self.is_empty(self.queue) else self.queue[0]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParentPosition(self, i):
        return int((i - 1) / 2)

    def getLeftChildPosition(self, i):
        return 2 * i + 1

    def getRightChildPosition(self, i):
        return 2 * i + 2

    def hasParent(self, i):
        return self.getParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        return self.getLeftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChildPosition(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def getMax(self):
        return self.heap[0]

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.getParentPosition(i)]):
            self.heap[i], self.heap[self.getParentPosition(i)] = self.heap[self.getParentPosition(i)], self.heap[i]
            i = self.getParentPosition(i) 

    def printHeap(self):
        print(self.heap)



class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def addToStart(self, newData):
        newNode = Node(newData)
        newNode.nextNode = self.head
        self.head = newNode

    def addToEnd(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        
        head = self.head
        while head.nextNode:
            head = head.nextNode
        head.nextNode = newNode

    def addInBetween(self, middleNode, newData):
      if middleNode is None:
         print("The mentioned node is absent.")
         return

      newNode = Node(newData)
      newNode.nextNode = middleNode.nextNode
      middleNode.nextNode = newNode
    
    def RemoveNode(self, removeKey):
        head = self.head
        if head is None:
            return
        elif head.data == removeKey:
            self.head = head.nextNode
            head = None
            return
        
        while head is not None:
            if head.data == removeKey:
                break
            prev = head
            head = head.nextNode

        prev.nextNode = head.nextNode
        head = None
    
    def check(self, data):
        head = self.head
        while head:
            if data == head.data:
                return True
            head = head.nextNode
        return False

    def get(self, dataIdx):
        head = self.head
        nodeIdx = 0
        while nodeIdx <= dataIdx:
            if nodeIdx == dataIdx:
                return head.data
            nodeIdx += 1
            head = head.nextNode