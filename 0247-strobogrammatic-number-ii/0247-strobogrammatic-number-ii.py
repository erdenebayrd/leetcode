class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        # 0 -> 0
        # 1 -> 1
        # 8 -> 8

        # 6 -> 9
        # 9 -> 6
        rotateMap = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

        # starting numbers can be 1, 8, 6, 9 when n > 1
        # step1: we'll build n // 2 numbers only at first
        # step2: add it's suffixes
        self.rotates = ["0", "1", "8", "6", "9"]
        self.result = ["1", "8", "6", "9"]
        
        # step 1:
        def build(rest: int) -> None:
            if rest <= 0:
                return
            current = []
            for i in range(len(self.result)):
                for j in range(len(self.rotates)):
                    current.append(self.result[i] + self.rotates[j])
            self.result = current[:]
            build(rest - 1)
        
        build(n // 2 - 1)
        # step 2:
        def getSecondHalf(sub: str) -> str:
            result = ""
            for i in range(len(sub) - 1, -1, -1):
                result += rotateMap[sub[i]]
            return result

        if n % 2 == 0: # if n is even
            for i in range(len(self.result)):
                secondHalf = getSecondHalf(self.result[i])
                self.result[i] = self.result[i] + secondHalf
        else:
            current = []
            for i in range(len(self.result)):
                firstHalf = self.result[i]
                secondHalf = getSecondHalf(firstHalf)
                for j in range(3):
                    middle = self.rotates[j]
                    current.append(firstHalf + middle + secondHalf)
            self.result = current[:]

        return self.result