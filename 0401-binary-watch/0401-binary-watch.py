class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
            
            3210
            ****.   <-- hour
            ******. <-- minute
            543210
            
            turnedOn = 1 
            Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        """

        result = []
        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    currentTime = str(hour)
                    if minute < 10:
                        currentTime = currentTime + ":0" + str(minute)
                    else:
                        currentTime = currentTime + ":" + str(minute)
                    result.append(currentTime)
        return result
                    