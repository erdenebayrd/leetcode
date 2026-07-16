from collections import deque

class TrieNode:
    def __init__(self) -> None:
        self.fail_link = None
        self.output_link = None
        self.word_count = 0
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.root.fail_link = self.root
    
    def add_word(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.word_count += 1
    
    def build_links(self) -> None:
        queue = deque()
        queue.append(self.root)
        while queue:
            parent = queue.popleft()
            for ch in parent.children:
                fail_link = parent.fail_link
                child = parent.children[ch]
                queue.append(child)
                while ch not in fail_link.children and fail_link != self.root:
                    fail_link = fail_link.fail_link
                child.fail_link = fail_link
                if ch in fail_link.children and fail_link.children[ch] != child:
                    child.fail_link = fail_link.children[ch]
                if child.fail_link.word_count > 0:
                    child.output_link = child.fail_link
                else:
                    child.output_link = child.fail_link.output_link

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        we can iterate through patterns array one by one

        checking and counting each pattern is included in word or not.
        m = len(pattern)
        k = len(pattern[i])
        n = len(word)
        time O(m * k * n)

        but we can use KMP or Z-algorithm to reduce time complexity a bit

        time O(m * k + m * n))
        space O(k + n) but we can reduce it using LCP on pattern only O(k)
        or we can use aho-corasick algo to reduce time again

        time O(n + m * k)
        space O(m * k)
        """
        # # approach 1 brute force
        # # time: O(n * m * k)
        # # space: O(1)
        # # method: brute force
        # m = len(patterns)
        # n = len(word)
        # count = 0
        # for i in range(m):
        #     count += patterns[i] in word
        # return count

        # # approach 2 KMP
        # # time: O(m * (n + k))
        # # space: O(k)
        # # method: KMP string pattern searching algo
        # m = len(patterns)
        # n = len(word)
        # count = 0
        # def kmp(pattern: str, text: str) -> bool:
        #     k = len(pattern)
        #     lcp = [0] * k
        #     length = 0
        #     for i in range(1, k):
        #         while length > 0 and pattern[length] != pattern[i]:
        #             length = lcp[length - 1]
        #         if pattern[length] == pattern[i]:
        #             length += 1
        #         lcp[i] = length
        #     length = 0
        #     for i in range(len(text)):
        #         while length > 0 and pattern[length] != text[i]:
        #             length = lcp[length - 1]
        #         if pattern[length] == text[i]:
        #             length += 1
        #         if length == len(pattern):
        #             return True
        #     return False
        
        # for i in range(m):
        #     count += kmp(patterns[i], word)
        # return count

        # approach 2's alternative (Z-algo)
        # time: O(m * (n + k))
        # space: O(k + n)
        # method: Z-Algorithm
        # n = len(word)
        # m = len(patterns)
        # count = 0
        
        # def z(pattern: str, text: str) -> bool:
        #     text = pattern + text
        #     n = len(text)
        #     z_values = [0] * n
        #     z_values[0] = n
        #     left = right = -1
        #     for i in range(1, n):
        #         if i <= right:
        #             z_values[i] = min(right - i + 1, z_values[i - left])
        #         while i + z_values[i] < n and text[z_values[i]] == text[i + z_values[i]]:
        #             z_values[i] += 1
        #         if i + z_values[i] - 1 > right:
        #             left = i
        #             right = i + z_values[i] - 1
        #     return max(z_values[len(pattern):]) >= len(pattern)

        # for pattern in patterns:
        #     count += z(pattern, word)
        
        # return count

        # approach 3 Aho-Corasick algo
        # time: O(m * k + n)
        # space: O(m * k)
        # method: Aho-Corasick 

        trie = Trie()
        for pattern in patterns:
            trie.add_word(pattern)
        trie.build_links()
        count = 0
        current = trie.root
        for ch in word:
            while ch not in current.children and current != trie.root:
                current = current.fail_link
            if ch in current.children:
                current = current.children[ch]
            
            count += current.word_count
            current.word_count = 0
            output_link = current.output_link

            while output_link and output_link.word_count > 0:
                count += output_link.word_count
                output_link.word_count = 0
                output_link = output_link.output_link

        return count