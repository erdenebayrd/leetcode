class Node:
    def __init__(self):
        self.index = 0
        self.arr = []
        self.next = None
        self.prev = None

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.node1 = Node()
        self.node1.arr = v1
        self.node2 = Node()
        self.node2.arr = v2
        self.node1.prev = self.node2
        self.node1.next = self.node2
        self.node2.prev = self.node1
        self.node2.next = self.node1
        self.current = self.node1

    def next(self) -> int:
        index = self.current.index
        value = self.current.arr[index]
        self.current.index += 1
        self.current = self.current.next
        return value

    def hasNext(self) -> bool:
        while self.current.index >= len(self.current.arr):
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.next
            if self.current == self.current.next:
                return self.current.index < len(self.current.arr)
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())