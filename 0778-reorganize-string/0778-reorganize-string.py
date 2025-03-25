class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
        arr = []
        for ch in cnt:
            num = cnt[ch]
            arr.append([-num, ch])
        
        res = "0"
        heapq.heapify(arr)
        while len(arr) > 0:
            top = heapq.heappop(arr)
            if res[-1] != top[1]:
                res += top[1]
                top[0] += 1
                if top[0] == 0:
                    continue
                heapq.heappush(arr, top)
            else:
                if len(arr) == 0:
                    return ""
                secondTop = heapq.heappop(arr)
                res += secondTop[1]
                heapq.heappush(arr, top)
                secondTop[0] += 1
                if secondTop[0] == 0:
                    continue
                heapq.heappush(arr, secondTop)
        return res[1:]