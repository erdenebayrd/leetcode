class RollingHash:
    def __init__(self, arr: list, base: int, mod: int) -> None:
        self.base = base
        self.mod = mod
        self.hash = [0] * len(arr)
        self.hash[0] = arr[0]
        self.base_power = [1] * len(arr)
        for i in range(1, len(arr)):
            self.hash[i] = (self.hash[i - 1] * base + arr[i]) % mod
            self.base_power[i] = (self.base_power[i - 1] * base) % mod
    
    def get_hash(self, left: int, right: int) -> int:
        if left == 0:
            return self.hash[right]
        return (self.hash[right] - self.hash[left - 1] * self.base_power[right - left + 1]) % self.mod

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(n * log n)
        # space: O(n)
        # method: Rabin Karp (Rolling Hash)
        n = len(nums1)
        m = len(nums2)

        nums = [(257, int(1e9 + 7)), (57, int(1e9 + 7)), (257, int(1e9 + 9)),  (57, int(1e9 + 9))]
        hashes = []
        for base, mod in nums:    
            nums1_hash = RollingHash(nums1, base, mod)
            nums2_hash = RollingHash(nums2, base, mod)
            hashes.append((nums1_hash, nums2_hash))

        def check(length: int, nums1_hash: "RollingHash", nums2_hash: "RollingHash") -> bool:
            seen = set()
            for i in range(length - 1, n):
                left, right = i - length + 1, i
                value = nums1_hash.get_hash(left, right)
                seen.add(value)
            
            for i in range(length - 1, m):
                left, right = i - length + 1, i
                value = nums2_hash.get_hash(left, right)
                if value in seen:
                    return True
            return False

        low, high = 0, n + 1
        while low + 1 < high:
            mid = (low + high) // 2 # length
            if all([check(mid, nums1_hash, nums2_hash) for nums1_hash, nums2_hash in hashes]):
                low = mid
            else:
                high = mid
        return low