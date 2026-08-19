class Solution:
    def maxNumberOfFamilies(self, n: int, reserved_seats: List[List[int]]) -> int:
        # time: O(len(reserved_seats))
        # space: O(len(reserved_seats))
        # method: implementation

        reserved = {}
        for row, seat in reserved_seats:
            if 2 <= seat <= 9:
                if row not in reserved:
                    reserved[row] = 0
                reserved[row] |= (1 << seat)
        
        result = (n - len(reserved)) * 2
        
        for row in reserved:
            seat = reserved[row]
            for shift in range(2, 7, 2):
                available = (seat >> shift) & ((1 << 4) - 1)
                if available == 0:
                    result += 1
                    break
        return result
