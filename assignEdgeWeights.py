from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        
        max_node = 1
        for u, v in edges:
            if u > max_node:
                max_node = u
            if v > max_node:
                max_node = v
                
        
        adj = [[] for _ in range(max_node + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        
        queue = deque([(1, 0, 0)])
        max_depth = 0
        
        while queue:
            node, parent, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            
            for neighbor in adj[node]:
                if neighbor != parent:
                    queue.append((neighbor, node, depth + 1))
                    
        if max_depth == 0:
            return 0
            
        return pow(2, max_depth - 1, MOD)
