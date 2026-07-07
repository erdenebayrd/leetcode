class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return n
        cur_sum = 0
        cur_val = []
        for ch in str(n):
            num = int(ch)
            if num == 0:
                continue
            cur_sum += num
            cur_val.append(ch)
        return int("".join(cur_val)) * cur_sum