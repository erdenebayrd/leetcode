class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        for i, x in enumerate(capacity):
            apples -= x
            if apples <= 0:
                return i + 1
        assert False
        return -1