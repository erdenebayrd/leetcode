class Solution:
    def romanToInt(self, s: str) -> int:
        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000        
        """
            we can just build a map (dictionary map)
            { # containing only single char as a key
                I: 1
                V: 5
                ....
            }
            what I can do is start from left to right of the string s
            lastCharacter is initially float('inf')
            when I started from left
            I can just add the map value and update lastCharacter
            if lastCharacter's integer value is lower than current integer value of the character
            we would decrement 2 times lastCharacter's value
            update lastCharacter
        """
        # time: O(N) N is number of characters in Roman Number
        # space: O(1)
        # method: simulation
        n = len(s)
        digit = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        result = 0
        lastCharacterValue = float('inf')
        for i in range(n):
            currentValue = digit[s[i]]
            result += currentValue
            if lastCharacterValue < currentValue:
                result -= 2 * lastCharacterValue
            lastCharacterValue = currentValue
        return result




















        # I -> 1
        # V -> 5
        # X -> 10
        # L -> 50
        # C -> 100
        # D -> 500
        # M -> 1000
        # valid roman interger [1, 3999]
        # MMM + CM + XC + IX = 3000 + 900 + 90 + 9 
        # 
        # -------------------------------------
        # IV -> I + V = 4
        # IX -> I + X = 9
        # XL -> X + L = 40
        # XC -> X + C = 90
        # CD -> C + D = 400
        # CM -> C + M = 900
        # time: O(N)
        # space: O(N)

        # specificPatterns = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        # regularPatterns = { "I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000 }
        # arr = []
        # for ch in s:
        #     arr.append(ch)
        
        # def replacePattern(pattern: str) -> int:
        #     result = 0
        #     if len(pattern) == 2:
        #         for index in range(1, len(arr)):
        #             if arr[index - 1] + arr[index] == pattern:
        #                 result += specificPatterns[pattern]
        #                 arr[index - 1] = ""
        #                 arr[index] = ""
        #     if len(pattern) == 1:
        #         for index in range(len(arr)):
        #             if arr[index] == pattern:
        #                 result += regularPatterns[pattern]
        #                 arr[index] = ""
        #     return result

        # result = 0
        # for key in specificPatterns:
        #     result += replacePattern(key)
        # for key in regularPatterns:
        #     result += replacePattern(key)

        # return result

        # time: O(N)
        # space: O(1)

        romanToInt = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        previousValue = 0
        currentValue = 0
        total = 0
        for ch in s: 
            currentValue = romanToInt[ch]
            if previousValue < currentValue:
                total -= previousValue
            else: # previousValue <= currentValue
                total += previousValue
            previousValue = currentValue
        total += currentValue
        return total