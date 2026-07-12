class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(arr)
        current_rank = 1
        ranks = {}
        for value in sorted_array:
            if value not in ranks:
                ranks[value] = current_rank
                current_rank += 1
        result = []
        for value in arr:
            result.append(ranks[value])
        return result