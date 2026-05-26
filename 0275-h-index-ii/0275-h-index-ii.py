class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # time: O(log N)
        # space: O(1)
        # method: binary search
        n = len(citations)
        low, high = -1, n
        while low + 1 < high:
            mid = (low + high) // 2
            h_papers = n - mid
            h_citation = citations[mid]
            if h_papers <= h_citation:
                high = mid
            else:
                low = mid
        result = n - high
        return result