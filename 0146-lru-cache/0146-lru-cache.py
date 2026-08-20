from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.ordered_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.ordered_dict:
            return -1
        self.ordered_dict.move_to_end(key, last=True)
        return self.ordered_dict.get(key)

    def put(self, key: int, value: int) -> None:
        self.ordered_dict[key] = value
        self.ordered_dict.move_to_end(key, last=True)
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)