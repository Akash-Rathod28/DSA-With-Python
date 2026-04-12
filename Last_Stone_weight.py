import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            difference = a - b
            if difference != 0:
                heapq.heappush(heap,-difference)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]        
