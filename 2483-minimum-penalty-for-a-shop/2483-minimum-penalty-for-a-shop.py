class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # if we close the shop at n'th hour
        n = len(customers)
        earliestHour = n
        penalty = 0
        for ch in customers:
            penalty += int(ch == "N")
        curPenalty = penalty
        for i in range(n - 1, -1, -1):
            # if close at i'th hour
            if customers[i] == "Y":
                curPenalty += 1
            else: # "N"
                curPenalty -= 1
            if curPenalty <= penalty:
                penalty = curPenalty
                earliestHour = i
        return earliestHour