class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time: O(N)
        # space: O(26)
        lastOccurrence = {ch: i for i, ch in enumerate(s)}
        start, end = 0, 0
        parts = []
        for i, ch in enumerate(s):
            end = max(end, lastOccurrence[ch])
            if i == end:
                parts.append(end - start + 1)
                start = end + 1
        return parts