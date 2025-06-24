class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        arr = {}
        for i in range(n):
            for j in range(n):
                if abs(i - j) <= k and nums[j] == key:
                    arr[i] = True
        # print(arr)
        return list(arr)