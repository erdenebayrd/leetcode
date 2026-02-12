class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: simple stack adhoc
        stack = []
        for asteroid in asteroids:
            while asteroid != 0 and stack and stack[-1] > 0 and asteroid < 0: # right and left means collision
                prevAsteroid = stack.pop()
                if abs(prevAsteroid) > abs(asteroid):
                    asteroid = prevAsteroid
                elif abs(prevAsteroid) == abs(asteroid):
                    asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)
        return stack
                    