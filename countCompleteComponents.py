from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                component_nodes = []
                
                while queue:
                    curr = queue.popleft()
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                num_vertices = len(component_nodes)
                is_complete = True
                for node in component_nodes:
                    if len(adj[node]) != num_vertices - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components += 1
                    
        return complete_components
