class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
            
            3210
            ****.   <-- hour
            ******. <-- minute
            543210
            
            turnedOn = 1 
            Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

            in total we have 10 Leds available. 
            O(N * 2^ N) N = 10 max value of turned on is 10
            O(2 ^ turnedOn) time has to be 19:01 ->> 7:01
            bitmask solution
        """

        def convertToTime(number: int) -> str:
            minute = 0
            hour = 0
            for index in range(6):
                if number & (1 << index):
                    minute += (1 << index)
            for index in range(4):
                if number & (1 << (index + 6)):
                    hour += (1 << index)
            if 0 <= hour <= 11 and 0 <= minute <= 59:
                result = str(hour) + ":"
                if minute < 10:
                    result = result + "0" + str(minute)
                else:
                    result = result + str(minute)
                return result
            return ""
        
        n = 10
        result = []
        for bitmask in range(1 << n):
            countOnes = 0
            for index in range(n):
                if (1 << index) & bitmask:
                    countOnes += 1
            if countOnes == turnedOn:
                candidate = convertToTime(bitmask)
                if candidate != "":
                    result.append(candidate)
        return result