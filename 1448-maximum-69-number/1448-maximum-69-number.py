class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        arr = []
        for ch in s:
            arr.append(ch)
        for i in range(len(arr)):
            if arr[i] == '6':
                arr[i] = '9'
                break
        return int("".join(arr))