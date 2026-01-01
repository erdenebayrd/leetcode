class Leaderboard:

    def __init__(self):
        self.arr = []

    def addScore(self, playerId: int, score: int) -> None:
        found = False
        for i in range(len(self.arr)):
            if playerId == self.arr[i][1]:
                self.arr[i][0] += score
                found = True
        if found is False:
            self.arr.append([score, playerId])

    def top(self, K: int) -> int:
        self.arr.sort()
        return sum([x for x, _ in self.arr[-K:]])

    def reset(self, playerId: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][1] == playerId:
                self.arr[i][0] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)