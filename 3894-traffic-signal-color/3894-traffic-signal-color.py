class Solution:
    def trafficSignal(self, timer: int) -> str:
        # time: O(1)
        # space: O(1)
        # method: if else
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        return "Invalid"