from collections import deque

class TrieNode:
    def __init__(self) -> None:
        self.word_count = 0
        self.failure_link = None
        self.output_link = None
        self.is_visited = False
        self.children = {} # key as character, value as TrieNode

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.root.failure_link = self.root
    
    def add_word(self, word: str) -> None:
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.word_count += 1
    
    def build_links(self) -> None: # call this function after adding patterns into the trie
        queue = deque()
        queue.append((self.root, self.root, None)) # current_node, father's failure link node, character of this node
        while queue:
            current_node, failure_node, character = queue.popleft()
            while character not in failure_node.children and failure_node != self.root:
                failure_node = failure_node.failure_link
            
            current_node.failure_link = failure_node
            if character in failure_node.children and failure_node.children[character] != current_node:
                current_node.failure_link = failure_node.children[character]
            
            current_node.output_link = current_node.failure_link.output_link
            if current_node.failure_link.word_count > 0:
                current_node.output_link = current_node.failure_link

            for child_character in current_node.children:
                child_node = current_node.children[child_character]
                queue.append((child_node, current_node.failure_link, child_character))

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # time: O(len(word) + len(len(patterns[i])))
        # space: O(len(len(patterns[i])))
        # method: Aho-Corasick
        trie = Trie()
        for pattern in patterns:
            trie.add_word(pattern)
        trie.build_links()
        
        count = 0
        current_node = trie.root
        for ch in word:
            while ch not in current_node.children and current_node != trie.root:
                current_node = current_node.failure_link
            
            if ch in current_node.children:
                current_node = current_node.children[ch]

            # amortized O(1)
            output_node = current_node
            while output_node and not output_node.is_visited:
                output_node.is_visited = True
                count += output_node.word_count
                output_node = output_node.output_link
            
        return count