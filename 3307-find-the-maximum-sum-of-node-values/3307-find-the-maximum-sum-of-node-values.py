class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xor_array = []
        nonxor_array = []
        for x in nums:
            if (x ^ k) > x:
                xor_array.append(x ^ k)
            else:
                nonxor_array.append(x)
        if len(xor_array) % 2 == 0 or len(xor_array) == 0:
            return sum(xor_array) + sum(nonxor_array)
        # print(xor_array)
        # print(nonxor_array)
        # xor_array.sort()
        # xor_min = xor_array[0]
        # print(xor_min)
        # xor_array = xor_array[1:]
        idx_xor = -1
        mn_xor = int(2e9)
        for i in range(len(xor_array)):
            cur = xor_array[i] - (xor_array[i] ^ k)
            if cur < mn_xor:
                mn_xor = cur
                idx_xor = i
        xor_min = xor_array[idx_xor]
        a = []
        for i in range(len(xor_array)):
            if i == idx_xor:
                continue
            a.append(xor_array[i])
        xor_array = a

        res = (xor_min ^ k) + sum(xor_array) + sum(nonxor_array)
        # print(res)
        if len(nonxor_array) == 0:
            return res
        idx = -1
        mn = int(2e9)
        for i in range(len(nonxor_array)):
            cur = nonxor_array[i] - (nonxor_array[i] ^ k)
            if cur < mn:
                mn = cur
                idx = i
        # print(idx, nonxor_array[idx])
        res1 = sum(xor_array)
        for i in range(len(nonxor_array)):
            if idx == i:
                continue
            res1 += nonxor_array[i]
        res1 += xor_min + (nonxor_array[idx] ^ k)
        return max(res, res1)