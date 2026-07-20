class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # time: O(N * 2 ^ N)
        # space: O(2 ^ N)
        # method: bitmask + brute force
        n = len(word)

        def abbrevation(bitmask: int) -> str:
            count = 0
            abbr = []
            for i in range(n):
                if bitmask & (1 << i):
                    count += 1
                else:
                    if count:
                        abbr.append(str(count))
                        count = 0
                    abbr.append(word[i])
            if count:
                abbr.append(str(count))
            return "".join(abbr)

        result = []
        for bitmask in range(1 << n):
            result.append(abbrevation(bitmask))
        return result