class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        # method: hashmap
        positions = defaultdict(list)
        for i in range(len(nums)):
            positions[nums[i]].append(i)
        
        result = float('inf')
        for value in positions:
            if len(positions[value]) < 3:
                continue
            for i in range(2, len(positions[value])):
                result = min(result, (positions[value][i] - positions[value][i - 2]) * 2)
        if result == float('inf'):
            result = -1
        return result