class Trie:
    def __init__(self) -> None:
        self.children = {}
    
    def insert(self, number: str) -> None:
        current = self.children
        for ch in number:
            if ch not in current:
                current[ch] = Trie()
            current = current[ch].children
    
    def count_prefix(self, number: str) -> int:
        current = self.children
        length = 0
        for ch in number:
            if ch not in current:
                return length
            length += 1
            current = current[ch].children
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # time: O(N + M)
        # space: O(N)
        # method: Trie
        trie = Trie()
        for number in arr1:
            trie.insert(str(number))
        
        result = 0
        for number in arr2:
            result = max(result, trie.count_prefix(str(number)))
        
        return result