class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        trainerIdx = 0
        res = 0
        for i in range(len(players)):
            while trainerIdx < len(trainers) and players[i] > trainers[trainerIdx]:
                trainerIdx += 1
            if trainerIdx < len(trainers):
                res += 1
                trainerIdx += 1
        return res