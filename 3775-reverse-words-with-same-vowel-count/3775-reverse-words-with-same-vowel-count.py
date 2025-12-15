class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        vowels = sum(1 for ch in arr[0] if ch in 'aeiou')
        for i in range(1, len(arr)):
            if vowels == sum(1 for ch in arr[i] if ch in 'aeiou'):
                arr[i] = arr[i][::-1]
        return " ".join(arr)