class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: hashmap + meet in the middle
        arr1 = []
        for x in nums1:
            for y in nums2:
                arr1.append(x + y)
        
        arr2 = []
        for x in nums3:
            for y in nums4:
                arr2.append(x + y)
        
        count = Counter(arr2)
        result = 0
        for x in arr1:
            need = -x
            result += count[need]
        return result