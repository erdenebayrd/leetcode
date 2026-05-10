class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        brute force solution would be selecting 3 different indices from nums array (i, j, k) where i < j < k then check it's lengths 
        if any sum of 2 of values is greater than or equal to the other one, can't say it's triangle
        otherwise it's an possible triangle sides

        but this would be O(N ^ 3) N is the length of given array

        we can use 2 pointers in here
        first sort the array by non-decreasing order
        then what if the first length is "i"th value
        then we try to choose, j, k indices from rest of the array indices where i < j < k

        lets say this is the array
          i
        [ 2 , 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7 ]
              j                 k
        """
        def isValid(i: int, j: int, k: int) -> bool:
            return nums[i] + nums[j] > nums[k]

        n = len(nums)
        nums.sort()
        result = 0
        for i in range(n - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                k = max(k, j)
                while k < n and isValid(i, j, k):
                    k += 1
                result += k - 1 - j
        return result