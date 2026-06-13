class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # time: O(N)
        # space: O(1)
        # method: adhoc

        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True