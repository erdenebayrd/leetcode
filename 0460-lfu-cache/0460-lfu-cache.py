class Node:
    def __init__(self, key: int = 0, value: int = 0, freq: int = 0) -> None:
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, freq: int = 0) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.prev = None
        self.next = None
        self.freq = freq
        self.keys = {}
    
    def put(self, key: int, value: int) -> "Node":
        self.keys[key] = Node(key=key, value=value, freq=self.freq)
        self.keys[key].next = self.tail
        self.keys[key].prev = self.tail.prev
        self.tail.prev.next = self.keys[key]
        self.tail.prev = self.keys[key]
        return self.keys[key]

    def delete(self, key: int) -> None:
        node = self.keys[key]
        del self.keys[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def popleft(self) -> "Node":
        node = self.head.next
        self.delete(node.key)
        return node
    
    def __len__(self) -> int:
        return len(self.keys)

class LFUCache:

    def __init__(self, capacity: int):
        self.head = LRUCache()
        self.tail = LRUCache()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keys = {}
        self.freqs = {0: self.head}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self.put(key, node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        current_freq = 0
        prev_lru_node = None
        if key in self.keys:
            node = self.keys[key]
            current_freq = node.freq
            del self.keys[key]

            lru_node = self.freqs[node.freq]
            lru_node.delete(key)
            prev_lru_node = lru_node
        
        if len(self.keys) == self.capacity:
            self.popleft()

        if current_freq + 1 not in self.freqs:
            lru_node = LRUCache(current_freq + 1)
            lru_node.prev = self.freqs[current_freq]
            lru_node.next = self.freqs[current_freq].next
            lru_node.next.prev = lru_node
            lru_node.prev.next = lru_node
            self.freqs[current_freq + 1] = lru_node
        
        lru_node = self.freqs[current_freq + 1]
        self.keys[key] = lru_node.put(key, value)
        if prev_lru_node is not None and len(prev_lru_node) == 0:
            prev_lru_node.prev.next = prev_lru_node.next
            prev_lru_node.next.prev = prev_lru_node.prev
            del self.freqs[prev_lru_node.freq]

        # if len(self.keys) > self.capacity:
        #     self.popleft()
    
    def popleft(self) -> None:
        lru_node = self.head.next # least frequently used lru
        node = lru_node.popleft()
        del self.keys[node.key]
        if len(lru_node) == 0:
            lru_node.prev.next = lru_node.next
            lru_node.next.prev = lru_node.prev
            del self.freqs[lru_node.freq]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)