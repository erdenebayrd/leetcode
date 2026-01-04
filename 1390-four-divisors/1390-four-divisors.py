class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = int(1e5)
        cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                cnt[j] += 1
        arr = []
        for i in range(1, n + 1):
            if cnt[i] == 4:
                arr.append([i, 0])
        for i in range(len(arr)):
            x, _ = arr[i]
            cur = -1
            for j in range(2, x):
                if x % j == 0:
                    cur = j
                    break
            arr[i][1] = 1 + cur + x // cur + x
        cnt = defaultdict(int)
        for x, y in arr:
            cnt[x] = y
        res = 0
        for x in nums:
            res += cnt[x]
        return res