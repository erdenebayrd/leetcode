class Solution:
    def minimumDistance(self, word: str) -> int:
        """
            brute force solution is to consider all the way to divide word into 2 piece of letters using bitmask
            and take the min cost one, which would take O(N * 2 ^ N) time complexity

            may be we can use DP solution here with below state
            at each character left to right of the given word
            so before we can type i'th character, 2 fingers at which character (A - Z)
            func(index, finger 1 position, finger 2 position)
            time complexity 26 * 26 * N
            where N is a number of chars in the given word
        """
        # time: O(26 * 26 * N)
        # space: O(26 * 26 * N)
        # method: DP

        n = len(word)

        def getPosition(ch: str) -> Tuple[int, int]:
            position = ord(ch) - ord('A')
            row = position // 6
            col = position % 6
            return (row, col)

        def calcDistance(ch: str, finger: str) -> int:
            if finger == "":
                return 0
            chx, chy = getPosition(ch)
            fx, fy = getPosition(finger)
            return abs(chx - fx) + abs(chy - fy)

        @cache
        def solve(index: int, finger1: str, finger2: str) -> int:
            if index >= n:
                return 0
            distance1 = calcDistance(word[index], finger1)
            distance2 = calcDistance(word[index], finger2)
            result = distance1 + solve(index + 1, word[index], finger2)
            result = min(result, distance2 + solve(index + 1, finger1, word[index]))
            return result
        
        return solve(0, "", "")