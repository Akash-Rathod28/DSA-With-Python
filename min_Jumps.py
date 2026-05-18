from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        
        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([(0, 0)])   
        visited = set([0])

        while queue:
            index, steps = queue.popleft()

            
            if index == n - 1:
                return steps

            neighbors = graph[arr[index]] + [index - 1, index + 1]

            for nei in neighbors:
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))

           
            graph[arr[index]].clear()
