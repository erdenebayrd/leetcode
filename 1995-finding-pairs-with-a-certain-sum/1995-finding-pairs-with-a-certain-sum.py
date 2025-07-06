class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.__cnt = defaultdict(int)
        for x in nums2:
            self.__cnt[x] += 1
        self.__nums1 = nums1
        self.__nums2 = nums2

    def add(self, index: int, val: int) -> None:
        currentVal = self.__nums2[index]
        self.__cnt[currentVal] -= 1
        currentVal += val
        self.__cnt[currentVal] += 1
        self.__nums2[index] = currentVal

    def count(self, tot: int) -> int:
        res = 0
        for x in self.__nums1:
            res += self.__cnt[tot - x]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)