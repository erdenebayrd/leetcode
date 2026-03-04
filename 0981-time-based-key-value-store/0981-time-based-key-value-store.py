"""
Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain
timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object.
- void set(String key, String value, int timestamp) Stores the key with the
value at the given timestamp.
- String get(String key, int timestamp) Returns a value such that set was called
previously with timestamp_prev <= timestamp. If there are multiple such values,
return the value with the largest timestamp_prev. If there are no values, return
"".

Example:
Input: ["TimeMap","set","get","get","set","get","get"]
       [
  [],
  ["foo","bar",1],
  ["foo",1],
  ["foo",3],
  ["foo","bar2",4],
  ["foo",4],
  ["foo",5]
]
Output: [null,null,"bar","bar",null,"bar2","bar2"]

key-value: {
    foo: [bar, 1], [bar2, 4]
}

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits
- 1 <= timestamp <= 10^7
- All timestamps of set are strictly increasing.
"""
import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self): # O(1)
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str: # O(log n) n is the size of array on the "key"
        if key not in self.dictionary:
            return ""
        # index = bisect.bisect_right(self.dictionary[key], timestamp) # is the array with strictly increasing timestamps with values
        low, high = -1, len(self.dictionary[key])
        while low + 1 < high:
            middle = (low + high) // 2
            midTimestamp, _ = self.dictionary[key][middle]
            if midTimestamp <= timestamp:
                low = middle
            else: # midTimestamp > timestamp
                high = middle
        index = low
        if index == -1:
            return ""
        _, value = self.dictionary[key][index]
        return value