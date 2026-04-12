class Node:
    def __init__(self, key=None, value=None, next=None, prev=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.tail = self.head = Node()
    
        self.size = 0
        self.capacity = capacity
        self.hashmap = {}        

    def append(self, key: int, value: int) -> None:
        node = Node(key=key, value=value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.hashmap[key] = self.tail
        self.size += 1

    def moveToEnd(self, key: int) -> None:
        currentNode = self.hashmap[key]
        
        prevNode = currentNode.prev
        nextNode = currentNode.next
        if nextNode is None: # already at end
            return
        
        prevNode.next = nextNode
        nextNode.prev = prevNode

        self.tail.next = currentNode
        currentNode.prev = self.tail
        currentNode.next = None

        self.tail = currentNode

    def popleft(self) -> None:
        node = self.head.next
        nextNode = node.next
        self.head.next = nextNode
        if nextNode is not None:
            nextNode.prev = self.head
        
        node.prev = None
        node.next = None
        del self.hashmap[node.key]
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.moveToEnd(key)
        return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            self.append(key=key, value=value)
        else:
            self.hashmap[key].value = value
            self.moveToEnd(key)
        
        while self.size > self.capacity:
            self.popleft()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)