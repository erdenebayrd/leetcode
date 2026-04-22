class Solution:
    def longestBalanced(self, s: str) -> int:
        # time: O(N)
        # space: O(N)
        # method: -1, 1 prefix sum, counting, greedy
        arr = []
        n = len(s)
        # print(n)
        for ch in s:
            if ch == '0':
                arr.append(-1)
            else:
                arr.append(1)
        total = Counter(arr)
        # print(total)
        # print(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
        # print(arr)
        pos = defaultdict(list)
        pos[0].append(-1)
        result = 0
        for i in range(n):
            # print(pos)
            # 0
            need = arr[i]
            # print(need, need in pos, 0)
            if need in pos:
                result = max(result, i - pos[need][0])
            
            # 2
            # arr[i] - x == 2
            need = arr[i] - 2
            # print(need, need in pos, 2)
            idx = 0
            while need in pos and idx < len(pos[need]):
                left = pos[need][idx]
                right = i
                zeros = (right - left - 2) // 2
                if total[-1] > zeros:
                    result = max(result, right - left)
                    break
                idx += 1
            
            # -2
            # arr[i] - x == -2
            need = arr[i] + 2
            # print(need, need in pos, -2)
            idx = 0
            while need in pos and idx < len(pos[need]):
                left = pos[need][idx]
                right = i
                ones = (right - left - 2) // 2
                if total[1] > ones:
                    # print(total[1], ones, total[1] > ones)
                    result = max(result, right - left)
                    break
                idx += 1
            
            pos[arr[i]].append(i)
            # if arr[i] not in pos:
            #     pos[arr[i]] = i

        return result