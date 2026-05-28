class TrieNode:
    def __init__(self):
        self.word_length = float("inf")
        self.word_index = float("inf")
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str, word_index: int) -> None: # O(len(word))
        current_node = self.root
        path = []
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
            path.append(current_node)
        
        if current_node.word_length > 1:
            current_node.word_length = 1
            current_node.word_index = word_index
        elif current_node.word_length == 1:
            current_node.word_index = min(current_node.word_index, word_index)
        
        
        for i in range(len(path) - 2, -1, -1):
            current_node = path[i]
            next_node = path[i + 1]
            if current_node.word_index == -1 or current_node.word_length > next_node.word_length + 1 or (current_node.word_length == next_node.word_length + 1 and current_node.word_index > next_node.word_index):
                current_node.word_index = next_node.word_index
                current_node.word_length = next_node.word_length + 1
    
    def find_index_of_longest(self, pattern: str) -> int:
        current_node = self.root
        for ch in pattern:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                break
        if current_node.word_index == float('inf'): # meaning root
            return -1
        return current_node.word_index
    
class Solution:
    def stringIndices(self, words_container: List[str], words_query: List[str]) -> List[int]:
        # time: O(N + M) N is total number of chars in words container, M is total number of chars in words query
        # space: O(N)
        # method: Trie with tuple (min length, index of word in a words_container)
        trie = Trie()
        shortest_length_index = 0
        for word_index, word in enumerate(words_container): # O(N)
            trie.insert(word[::-1], word_index)
            if len(words_container[shortest_length_index]) > len(word):
                shortest_length_index = word_index
        
        result = []
        for pattern in words_query: # O(M)
            index = trie.find_index_of_longest(pattern[::-1])
            if index == -1:
                index = shortest_length_index
            result.append(index)

        return result