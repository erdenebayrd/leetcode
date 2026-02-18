from functools import cache
from collections import defaultdict

class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
    def insert(self, node, word):
        n = len(word)
        for i in range(n):
            ch = word[i]
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # tc: O(N ^ 2) canBreak startIndex be [1, n], inside each recursive, for loop from 1 to n 
        # space: O(M) M is total character of wordDict
        n = len(s)
        trie = Trie()
        for word in wordDict:
            trie.insert(trie, word)
        
        @cache
        def canBreak(startIndex):
            if startIndex >= n:
                return True
            node = trie # start from root
            for index in range(startIndex, n):
                ch = s[index]    
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.isWord:
                    if canBreak(index + 1):
                        return True
            return False
        
        return canBreak(0)