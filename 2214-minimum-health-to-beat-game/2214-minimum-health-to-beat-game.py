class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy
        return sum(damage) - min(max(damage), armor) + 1