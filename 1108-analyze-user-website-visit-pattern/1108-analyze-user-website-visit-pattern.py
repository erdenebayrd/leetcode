class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        users = defaultdict(lambda: defaultdict(list))
        for i in range(n):
            users[username[i]][website[i]].append(timestamp[i])

        def solve(webs: List[str]) -> int:
            visStamp = defaultdict(int)
            res = 0
            for user in users:
                check = 0
                for web in webs:
                    idx = bisect_left(users[user][web], visStamp[user] + 1)
                    if idx < len(users[user][web]):
                        visStamp[user] = users[user][web][idx]
                        check += 1
                if check == len(webs):
                    res += 1
            # ['home', 'about', 'career']
            # print("-" * 10)
            # print(webs)
            # print(res)
            # print("-" * 10)
            return res

        def getLowerLexo(l1: List[str], l2: List[str]) -> List[str]:
            assert len(l1) == len(l2)
            for i in range(len(l1)):
                if l1[i] < l2[i]:
                    return l1
                elif l1[i] > l2[i]:
                    return l2
            return l1

        res = []
        cur = 0
        webs = list(set(website))
        for user in users:
            for web in webs:
                users[user][web].sort()
        for web1 in webs:
            for web2 in webs:
                for web3 in webs:
                    cnt = solve([web1, web2, web3])
                    if cnt == 0:
                        continue
                    if cnt == cur:
                        res = getLowerLexo(res, [web1, web2, web3])
                    elif cur < cnt:
                        cur = cnt
                        res = [web1, web2, web3]
        # print(solve(["about","career","home"]))
        return res