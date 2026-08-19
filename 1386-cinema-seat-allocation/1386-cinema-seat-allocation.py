class Solution:
    def maxNumberOfFamilies(self, n: int, reserved_seats: List[List[int]]) -> int:
        # time: O(len(reserved_seats))
        # space: O(len(reserved_seats))
        # method: implementation

        def is_available(row: int, left: int, right: int) -> bool:
            for seat in range(left, right + 1):
                if seat in reserved[row]:
                    return False
            return True

        reserved = {}
        for row, seat in reserved_seats:
            if row not in reserved:
                reserved[row] = set()
            if seat == 1 or seat == 10:
                continue
            reserved[row].add(seat)
        
        result = (n - len(reserved)) * 2
        for row in reserved:
            if len(reserved[row]) == 0:
                result += 2
                continue

            for left in range(2, 7, 2):
                if is_available(row, left, left + 3):
                    result += 1
                    break
        return result