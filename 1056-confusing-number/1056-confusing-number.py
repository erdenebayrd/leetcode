class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0:
            return False
        invalid = [2, 3, 4, 5, 7]
        arr = []
        b = []
        m = n
        flag = False
        while m > 0:
            x = m % 10
            b.append(x)
            if x in invalid:
                return False
            if x == 9:
                x = 6
            elif x == 6:
                x = 9
            arr.append(x)
            m //= 10
        b = list(reversed(b))
        for i in range(len(arr)):
            if b[i] != arr[i]:
                return True
        return False