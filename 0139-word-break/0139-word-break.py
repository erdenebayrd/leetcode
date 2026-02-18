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
        n = len(s)
        trie = Trie()
        for word in wordDict:
            trie.insert(trie, word)
        
        @cache
        def canBreak(startIndex):
            if startIndex >= n:
                return True
            result = False
            node = trie
            for index in range(startIndex, n):
                ch = s[index]
                if ch in node.children and node.children[ch].isWord:
                    result |= canBreak(index + 1)
                if ch not in node.children:
                    break
                node = node.children[ch]

            return result
        
        return canBreak(0)