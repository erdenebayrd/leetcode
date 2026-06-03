class Node:
    def __init__(self) -> None:
        self.keys = set()
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append_after(self, ref: "Node") -> "Node": # returns node reference
        node = Node()
        node.prev = ref
        node.next = ref.next
        ref.next.prev = node
        ref.next = node
        return node
    
    def append_before(self, ref: "Node") -> "Node": # returns node reference
        return self.append_after(ref.prev)
        
    def remove(self, ref: "Node") -> None:
        ref.prev.next = ref.next
        ref.next.prev = ref.prev

class AllOne:

    def __init__(self):
        self.freq = LinkedList()
        self.key_refs = {} # key as key string, value as reference of "frequency" linkedlist
        self.counter_refs = {} # key as frequency number (integer), value as a ref of "frequency" linkedlist
        self.counter = defaultdict(int) # current count of keys

    def __remove(self, frequency: int, key: str) -> None:
        if frequency == 0:
            return
        self.counter_refs[frequency].keys.remove(key)
        # self.key_refs[key] already updated when __add() called, no need to update self.key_refs[key]
        # except frequency equal to 1 when __remove() called
        if frequency == 1:
            del self.key_refs[key]

        if len(self.counter_refs[frequency].keys) == 0:
            self.freq.remove(self.counter_refs[frequency])
            del self.counter_refs[frequency]
    
    def __add(self, frequency: int, key: str) -> None:
        if frequency == 0:
            return
        if frequency not in self.counter_refs:
            ref = None
            if frequency - 1 in self.counter_refs:
                ref = self.freq.append_after(self.counter_refs[frequency - 1])
            elif frequency + 1 in self.counter_refs:
                ref = self.freq.append_before(self.counter_refs[frequency + 1])
            else: # first time appending
                ref = self.freq.append_after(self.freq.head)
            self.counter_refs[frequency] = ref
        self.key_refs[key] = self.counter_refs[frequency]
        self.counter_refs[frequency].keys.add(key)

    def inc(self, key: str) -> None:
        self.counter[key] += 1
        self.__add(self.counter[key], key)
        self.__remove(self.counter[key] - 1, key)

    def dec(self, key: str) -> None:
        self.counter[key] -= 1
        self.__add(self.counter[key], key)
        self.__remove(self.counter[key] + 1, key)
        if self.counter[key] == 0:
            del self.counter[key]

    def getMaxKey(self) -> str:
        _prev = self.freq.tail.prev
        if _prev == self.freq.head:
            return ""
        return next(iter(_prev.keys))

    def getMinKey(self) -> str:
        _next = self.freq.head.next
        if _next == self.freq.tail:
            return ""
        return next(iter(_next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()