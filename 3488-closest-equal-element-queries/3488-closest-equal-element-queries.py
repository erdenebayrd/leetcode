class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # time: O(Q)
        # space: O(N)
        # method: hashmap indexing
        n = len(nums)
        def dist(i: int, j: int) -> int:
            if i > j:
                i, j = j, i
            result = j - i
            result = min(result, i + n - j)
            return result

        pos = defaultdict(list)
        indices = defaultdict(int)
        for i in range(len(nums)):
            pos[nums[i]].append(i)
            indices[i] = len(pos[nums[i]]) - 1
        
        result = []
        for index in queries:
            value = nums[index]
            idx = indices[index]
            if len(pos[value]) == 1:
                result.append(-1)
            else:
                m = len(pos[value])
                closest = dist(pos[value][idx], pos[value][(idx - 1) % m])
                closest = min(closest, dist(pos[value][idx], pos[value][(idx + 1) % m]))
                result.append(closest)
        return result