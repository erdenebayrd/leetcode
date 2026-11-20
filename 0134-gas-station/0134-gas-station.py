class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # time: O(n)
        # space: O(n)
        # method: SWAG prefix sum
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        prefix = diff + diff
        for i in range(1, 2 * n):
            prefix[i] += prefix[i - 1]
        
        inf = float('inf')
        current = 0
        left = []
        right = prefix[:n]
        right_min = inf

        for i in range(n):
            if not left:
                while right:
                    value = right.pop()
                    if not left:
                        left.append(value)
                    else:
                        left.append(min(left[-1], value))
                right_min = inf
            
            if current <= min(right_min, left[-1]):
                return i
            
            current = prefix[i]
            left.pop()
            right.append(prefix[i + n])
            right_min = min(right_min, right[-1])
        
        return -1