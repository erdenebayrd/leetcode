class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: sort + greedy
        n = len(aliceValues)
        scores = []
        for i in range(n):
            value = aliceValues[i] + bobValues[i]
            index = i
            scores.append([value, index])
        
        scores.sort(reverse=True)
        alice = 0
        bob = 0
        for i in range(n):
            index = scores[i][1]
            if i & 1:
                bob += bobValues[index]
            else:
                alice += aliceValues[index]
        
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        return 0