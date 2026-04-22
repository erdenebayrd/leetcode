class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # time: O(N * M * len(word))
        # space: O(1)
        # method: brute force
        
        def distance(word: str, target: str) -> int:
            n = len(word)
            cost = 0
            for i in range(n):
                if word[i] != target[i]:
                    cost += 1
            return cost
        
        result = []
        for word in queries:
            for target in dictionary:
                if distance(word, target) <= 2:
                    result.append(word)
                    break
        return result