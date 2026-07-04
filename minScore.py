from collections import deque, defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
