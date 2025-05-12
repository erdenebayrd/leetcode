class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or (digits[k] & 1 == 1):
                        continue
                    seen.add(int(str(digits[i]) + str(digits[j]) + str(digits[k])))
        return sorted(list(seen))