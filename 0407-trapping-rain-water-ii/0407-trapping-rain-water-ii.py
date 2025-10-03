class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        rows, cols = len(height_map), len(height_map[0])
      
        visited = [[False] * cols for _ in range(rows)]
      
        min_heap = []
      
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (height_map[i][j], i, j))
                    visited[i][j] = True
      
        trapped_water = 0
      
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
      
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    trapped_water += max(0, height - height_map[nx][ny])
                  
                    visited[nx][ny] = True
                  
                    heappush(min_heap, (max(height, height_map[nx][ny]), nx, ny))
      
        return trapped_water
