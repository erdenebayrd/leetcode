class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: int(x[1]))
        users = {}
        for i in range(numberOfUsers):
            users[i] = []
        for t, timestamp, ids in events:
            if t == "OFFLINE":
                users[int(ids)].append(int(timestamp))
        mentions = [0] * numberOfUsers
        delta = 0
        for t, timestamp, ids in events:
            if t == "OFFLINE":
                continue
            if ids == "ALL":
                delta += 1
            elif ids == "HERE":
                for i in range(numberOfUsers):
                    if len(users[i]) == 0:
                        mentions[i] += 1
                        continue
                    idx = bisect_right(users[i], int(timestamp)) - 1
                    if idx == -1:
                        mentions[i] += 1
                        continue
                    if users[i][idx] + 59 >= int(timestamp):
                        continue
                    mentions[i] += 1
            else:
                ids = ids.replace("id", "").split(" ")
                for idx in ids:
                    mentions[int(idx)] += 1
        for i in range(numberOfUsers):
            mentions[i] += delta
        return mentions