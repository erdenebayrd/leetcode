class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # time: O(N + M)
        # space: O(N)
        # method: ad-hoc
        n = len(list1)
        m = len(list2)
        pos = {}
        for i in range(n):
            pos[list1[i]] = i
        minDistance = float('inf')
        for i in range(m):
            text = list2[i]
            if text in pos:
                minDistance = min(minDistance, i + pos[text])
        result = []
        for i in range(m):
            text = list2[i]
            if text in pos and minDistance == i + pos[text]:
                result.append(text)
        return result