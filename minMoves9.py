from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        R, C = len(classroom), len(classroom[0])
        start = None
        targets = []
        
        for r in range(R):
            for c in range(C):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    targets.append((r, c))
                    
        if not start:
            return 0
        if not targets:
            return 0

        target_map = {pos: i for i, pos in enumerate(targets)}
        all_collected = (1 << len(targets)) - 1
        
        queue = deque([(start[0], start[1], energy, 0, 0)])
        visited = {(start[0], start[1], energy, 0)}
        
        while queue:
            r, c, e, mask, steps = queue.popleft()
            
            if mask == all_collected:
                return steps
            
            if e == 0:
                continue
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    next_e = energy if cell == 'R' else e - 1
                    next_mask = mask | (1 << target_map[(nr, nc)]) if (nr, nc) in target_map else mask
                    
                    state = (nr, nc, next_e, next_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, next_e, next_mask, steps + 1))
                        
        return -1
