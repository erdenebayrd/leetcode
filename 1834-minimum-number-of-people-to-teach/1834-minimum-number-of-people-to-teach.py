class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        langs = [None]
        for i in range(m):
            langs.append(set(languages[i]))
        # print(langs)
        friends = set()
        for u, v in friendships:
            if langs[u].isdisjoint(langs[v]) is False: # ignore if there is at least one element in common (they can communicate)
                continue
            friends.add(u)
            friends.add(v)
        # print(friends)
        res = m
        for i in range(1, n + 1): # will tech i'th language to them all who doesn't know it.
            cost = 0
            for user in friends:
                if i not in langs[user]:
                    cost += 1
            res = min(cost, res)
        return res