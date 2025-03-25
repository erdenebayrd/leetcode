class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = []
        teams = votes[0]
        teamOrder = {}
        for order, team in enumerate(teams):
            cur = [0] * len(teams)
            cur.append(team)
            rank.append(cur)
            teamOrder[team] = order
        # print(rank)
        for vote in votes:
            for i, ch in enumerate(vote):
                rank[teamOrder[ch]][i] -= 1
        rank.sort()
        return "".join([item[-1] for item in rank])