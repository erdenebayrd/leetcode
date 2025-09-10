class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # time: O(N * M)
        # space: O(N * M)
        m = len(languages)
        langs = [None]
        for i in range(m):
            langs.append(set(languages[i]))
        # print(langs)
        users = set()
        for u, v in friendships:
            if langs[u].isdisjoint(langs[v]) is False: # ignore if there is at least one element in common (they can communicate)
                continue
            users.add(u)
            users.add(v)
        # print(users)
        res = m
        for i in range(1, n + 1): # will tech i'th language to them all who doesn't know it.
            cost = 0
            for user in users:
                if i not in langs[user]:
                    cost += 1
            res = min(cost, res)
        return res