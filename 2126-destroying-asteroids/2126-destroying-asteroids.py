class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in range(len(asteroids)):
            if mass < asteroids[i]:
                return False
            mass += asteroids[i]
        return True