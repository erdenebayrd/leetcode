class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        # len(a) <= len(b)
        a = "0" * (len(b) - len(a)) + a
        # lengths are equal
        a = "0" + a
        b = "0" + b
        n = len(a)
        result = []
        remembered = 0
        for i in range(n - 1, -1, -1):
            first = ord(a[i]) - ord('0')
            second = ord(b[i]) - ord('0')
            # "111"
            #   +
            # "011"
            # 1010
            # rem = 1
            total = first + second + remembered
            result.append(chr(total % 2 + ord('0')))
            remembered = total // 2
        while result and result[-1] == '0':
            result.pop()
        result = result[::-1]
        result = "".join(result)
        if result == "":
            result = "0"
        return result