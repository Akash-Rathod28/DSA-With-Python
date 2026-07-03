from typing import List
import heapq

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        max_cost = 0
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                if cost > max_cost:
                    max_cost = cost
                    
        def can_achieve(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                curr_cost, u = heapq.heappop(pq)
                if u == n - 1:
                    return curr_cost <= k
                if curr_cost > dist[u]:
                    continue
                for v, cost in adj[u]:
                    if cost >= mid:
                        next_cost = curr_cost + cost
                        if next_cost < dist[v] and next_cost <= k:
                            dist[v] = next_cost
                            heapq.heappush(pq, (next_cost, v))
            return dist[n - 1] <= k

        low, high = 0, max_cost
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
