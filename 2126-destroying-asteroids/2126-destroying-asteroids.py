class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        m = max(asteroids)
        count = [0] * (m + 1)
        for sz in asteroids:
            count[sz] += 1
        
        for i in range(1, m + 1):
            if count[i] == 0:
                continue
            if mass < i:
                return False
            mass += count[i] * i
        return True