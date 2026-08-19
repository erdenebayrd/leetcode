class Node:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keys = {}
    
    def __delete(self, key: int) -> None:
        if key not in self.keys:
            return
        node = self.keys[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.keys[key]
    
    def __append(self, key: int, value: int) -> None:
        node = Node(key=key, value=value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.keys[key] = node

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        value = self.keys[key].value
        self.__delete(key)
        self.__append(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.__delete(key)
        self.__append(key, value)

    def popleft(self) -> None:
        if self.head.next == self.tail:
            return
        node = self.head.next
        del self.keys[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def __len__(self) -> int:
        return len(self.keys)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        return self.linked_list.get(key)

    def put(self, key: int, value: int) -> None:
        self.linked_list.put(key, value)
        if len(self.linked_list) > self.capacity:
            self.linked_list.popleft()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)