class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.__cnt = defaultdict(int)
        for x in nums2:
            self.__cnt[x] += 1
        self.__nums1 = nums1
        self.__nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.__cnt[self.__nums2[index]] -= 1
        self.__nums2[index] += val
        self.__cnt[self.__nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for x in self.__nums1:
            res += self.__cnt[tot - x]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)