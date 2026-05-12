class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: hashmap count
        count = Counter(nums1)
        result = []
        for x in nums2:
            if x not in count:
                continue
            result.append(x)
            count[x] -= 1
            if count[x] == 0:
                del count[x]
        return result