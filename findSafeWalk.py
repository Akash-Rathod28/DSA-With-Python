from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_loss = [[float('inf')] * n for _ in range(m)]
        queue = deque([(0, 0)])
        min_loss[0][0] = grid[0][0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                break
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_loss = min_loss[r][c] + grid[nr][nc]
                    if next_loss < min_loss[nr][nc]:
                        min_loss[nr][nc] = next_loss
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        
        return health - min_loss[m-1][n-1] >= 1
