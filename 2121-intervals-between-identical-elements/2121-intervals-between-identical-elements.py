class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: hashmap
        def sumDistances(indices: List[int]) -> int: # indices of identical elements in the nums
            if len(indices) == 1:
                return [0]
            result = []
            prefixSum = 0
            suffixSum = sum(indices)
            n = len(indices)
            for i in range(n):
                index = indices[i]
                suffixSum -= index
                value = index * (2 * i - n + 1) + suffixSum - prefixSum
                result.append(value)
                prefixSum += index
            return result
        
        n = len(nums)
        indices = defaultdict(list)
        for i in range(n):
            indices[nums[i]].append(i)
        
        result = [0] * n
        for value in indices:
            distances = sumDistances(indices[value])
            for i, index in enumerate(indices[value]):
                result[index] = distances[i]
        return result