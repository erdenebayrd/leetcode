class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        n = len(phrases)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                arr1 = phrases[i].split(" ")
                arr2 = phrases[j].split(" ")
                if arr1[-1] == arr2[0]: # arr1 + arr2
                    res.append(" ".join(arr1[:-1] + arr2))
                if arr2[-1] == arr1[0]: # arr2 + arr1
                    res.append(" ".join(arr2[:-1] + arr1))
        res = list(set(res))
        res.sort()
        return res