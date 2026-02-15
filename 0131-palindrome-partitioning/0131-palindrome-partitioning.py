class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Input: s = "aab"
        # Output: [["a","a","b"],["aa","b"]]

        # aab -> a_a_b
        #         0 1 => aa b
        #         there is 2 ^ (n - 1) possible splittings.
        # every possible splitter is active, we iterate through N, checking all partitions are palidrome or not
        # time: O(N ^ 2 (N - 1)) but we could just say O(N * 2 ^ N)
        # space: O(N) since we don't need to store all possible splitted string parts (we could just store one at the time)

        # isPalindrome function to check whether the sting between left and right indexes is palindrome or not
        # iterate from 00000000000 -> 00000000001 -> 00000000010 -> 00000000011 -> 00000000100 -> .... 11111111111. 
        # at 1 we use the splitter for example: 00000000010 ["pabcasdfasdfa", "sd"] is palindrome or not, if there is at least one element which is not palindrome, we would just ignore this partition.
        # otherwise we would add ["aa", "b"], ["a", "a", "b"] splitted strings into result array etc

        def isPalindrome(left: int, right: int) -> bool: # O(N)
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # result = []
        # n = len(s) # aab n = 3 -> 2 ^ 2 = 4 total options to split 
        # for bit in range(1 << (n - 1)): # 00 -> 01 -> 10 -> 11 O(2 ^ N)
        #     indices = [] # contains [left, right] indexes of s. For example: aab, [[0, 0], [1, 2]] = [a, ab]
        #     left, right = 0, n - 1          #                                  1   0
        #     for indexOfBit in range(n - 1): # indexOfBit = 3 means 11 => a,  a,  b # 10 O(N)
        #        # Left                                                        ^
        #        # Right                                                   ^
        #         if bit & (1 << indexOfBit): # we would use indexOfBit'th splitter
        #             right = indexOfBit
        #             indices.append([left, right])
        #             left = right + 1
        #     indices.append([left, n - 1])
        #     # print(indices)
        #     palindrome = True
        #     for left, right in indices:
        #         palindrome &= isPalindrome(left, right)
        #     if palindrome is True:
        #         # print(indices)
        #         nestedResult = []
        #         for left, right in indices:
        #             nestedResult.append(s[left:right + 1])
        #         result.append(nestedResult)
        # # time: O(N * 2 ^ N)
        # # space: O(N * 2 ^ N)
        # return result

        # --------------------------------------------- Recursive method ---------------------------------------------
        result = []
        currentResult = []
        n = len(s)
        def palindromeParition(startIndex: int) -> None:
            if startIndex == n:
                result.append(currentResult[:])
                return
            for rightIndex in range(startIndex, n):
                if isPalindrome(startIndex, rightIndex) is True:
                    currentResult.append(s[startIndex:rightIndex + 1])
                    palindromeParition(rightIndex + 1)
                    currentResult.pop()
        
        palindromeParition(0)
        return result