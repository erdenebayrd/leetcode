class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = defaultdict(int)
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            cnt[key] += 1
        mx = max(cnt.values())
        return sum(1 for v in cnt.values() if v == mx)