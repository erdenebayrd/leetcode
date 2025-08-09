class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # time: O(N ^ 2)
        # space: O(N)
        # method: n pointers
        cnt = defaultdict(int)
        for row in mat:
            for val in row:
                cnt[val] += 1
                if cnt[val] == len(mat):
                    return val
        return -1