# import random

# class RollingHash:
#     def __init__(self, arr: list, base: int, mod: int) -> None:
#         self.base = base
#         self.mod = mod
#         self.hash = [0] * len(arr)
#         self.hash[0] = arr[0]
#         self.base_power = [1] * len(arr)
#         for i in range(1, len(arr)):
#             self.hash[i] = (self.hash[i - 1] * base + arr[i]) % mod
#             self.base_power[i] = (self.base_power[i - 1] * base) % mod

#     def get_hash(self, left: int, right: int) -> int:
#         if left == 0:
#             return self.hash[right]
#         return (self.hash[right] - self.hash[left - 1] * self.base_power[right - left + 1]) % self.mod

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(n * log n)
        # space: O(n)
        # method: suffix array lcp (kasai)

        def count_sort(arr: list, key: int) -> list:
            n = len(arr)
            count = [0] * (n + 1) # since we use -1
            for i in range(n):
                count[arr[i][key] + 1] += 1
            for i in range(1, n + 1):
                count[i] += count[i - 1]
            bucket = [-1] * n
            for i in range(n - 1, -1, -1):
                value = arr[i][key] + 1
                count[value] -= 1
                bucket[count[value]] = arr[i]
            return bucket

        def radix_sort(arr: list) -> list:
            ranks = count_sort(arr, 1)
            ranks = count_sort(ranks, 0)
            return ranks

        def build_sa(arr: list) -> list: # returns suffix array
            n = len(arr)
            ranks = [(arr[i], -1, i) for i in range(n)]
            ranks.sort()
            for bit in range(n.bit_length()):
                updated_ranks = [0] * n
                indices = [0] * n
                for i in range(1, n):
                    prev_first_rank, prev_second_rank, _ = ranks[i - 1]
                    curr_first_rank, curr_second_rank, sa_index = ranks[i]
                    indices[sa_index] = i
                    updated_ranks[i] = updated_ranks[i - 1]
                    if prev_first_rank != curr_first_rank or prev_second_rank != curr_second_rank:
                        updated_ranks[i] += 1
            
                # update ranks array
                for i in range(n):
                    first_rank, second_rank, sa_index = ranks[i]
                    first_rank = updated_ranks[i]
                    second_rank = -1
                    if sa_index + (1 << bit) < n:
                        second_rank = updated_ranks[indices[sa_index + (1 << bit)]]
                    ranks[i] = (first_rank, second_rank, sa_index)
                
                ranks = radix_sort(ranks)
            sa = [sa_index for _, _, sa_index in ranks]
            return sa
        
        def calc_lcp(sa: list, arr: list) -> list:
            n = len(sa)
            lcp = [0] * n
            indices = [-1] * n
            for i in range(n):
                indices[sa[i]] = i
            
            prev_matched = 0
            for i in range(n):
                curr = indices[i]
                if curr == 0:
                    continue

                prev = curr - 1

                matched = 0
                if prev_matched:
                    matched = prev_matched - 1
                while sa[curr] + matched < n and sa[prev] + matched < n and arr[sa[prev] + matched] == arr[sa[curr] + matched]:
                    matched += 1
                prev_matched = matched
                lcp[curr] = matched
            
            return lcp


        n = len(nums1)
        arr = nums1 + [float("-inf")] + nums2
        sa = build_sa(arr)
        lcp = calc_lcp(sa, arr)

        # print(arr)
        # print('-' * 100)
        # for i in range(len(sa)):
        #     print(f"{lcp[i]}:", sa[i], arr[sa[i]:])
        # print('-' * 100)

        result = 0
        for i in range(1, len(lcp)):
            prev_index = sa[i - 1]
            curr_index = sa[i]
            length = lcp[i]
            if (prev_index < n and curr_index > n) or (prev_index > n and curr_index < n):
                result = max(result, length)
        return result

        # # time: O(n * log n)
        # # space: O(n)
        # # method: Rabin Karp (Rolling Hash)
        # n = len(nums1)
        # m = len(nums2)
        # base = int(1e9)
        # mods = [base + number for number in [7, 9, 21]]
        # bases = [random.SystemRandom().randint(257, mod - 2) for mod in mods]
        # hashes = []
        # for base, mod in zip(bases, mods):
        #     nums1_hash = RollingHash(nums1, base, mod)
        #     nums2_hash = RollingHash(nums2, base, mod)
        #     hashes.append((nums1_hash, nums2_hash))

        # def check(length: int, nums1_hash: "RollingHash", nums2_hash: "RollingHash") -> bool:
        #     seen = set()
        #     for i in range(length - 1, n):
        #         left, right = i - length + 1, i
        #         value = nums1_hash.get_hash(left, right)
        #         seen.add(value)
            
        #     for i in range(length - 1, m):
        #         left, right = i - length + 1, i
        #         value = nums2_hash.get_hash(left, right)
        #         if value in seen:
        #             return True
        #     return False

        # low, high = 0, n + 1
        # while low + 1 < high:
        #     mid = (low + high) // 2 # length
        #     if all([check(mid, nums1_hash, nums2_hash) for nums1_hash, nums2_hash in hashes]):
        #         low = mid
        #     else:
        #         high = mid
        # return low