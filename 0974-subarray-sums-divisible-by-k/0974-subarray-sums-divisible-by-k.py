class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        # method: hashmap + prefix sum
        n = len(nums)
        
        result = 0
        count = {0: 1}
        current = 0
        for i in range(n):
            current = (current + nums[i]) % k
            if current in count:
                result += count[current]
                count[current] += 1
            else:
                count[current] = 1
            
        return result