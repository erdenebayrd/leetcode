class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = []
        for i in nums:
            if i < pivot:
                arr.append(i)
        for i in nums:
            if i == pivot:
                arr.append(i)
        for i in nums:
            if i > pivot:
                arr.append(i)
        for i in range(len(nums)):
            nums[i] = arr[i]
        return nums