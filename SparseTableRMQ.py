from heapq import heappush, heappop

class SparseTableRMQ:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.lg = [0] * (n + 1)
        for i in range(2, n + 1):
            self.lg[i] = self.lg[i >> 1] + 1
            
        LOG = self.lg[n] + 1
        self.f_max = [[0] * LOG for _ in range(n)]
        self.f_min = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            self.f_max[i][0] = nums[i]
            self.f_min[i][0] = nums[i]
            
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                self.f_max[i][j] = max(self.f_max[i][j-1], self.f_max[i + (1 << (j-1))][j-1])
                self.f_min[i][j] = min(self.f_min[i][j-1], self.f_min[i + (1 << (j-1))][j-1])
                
    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(self.f_max[l][k], self.f_max[r - (1 << k) + 1][k])
        
    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(self.f_min[l][k], self.f_min[r - (1 << k) + 1][k])


class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        st = SparseTableRMQ(nums)
        pq = []
        
        # Seed the max-heap with the absolute maximum subarray for each left boundary 'l'
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heappush(pq, (-val, l, n - 1))
            
        ans = 0
        
        # Pop the k largest distinct subarrays
        for _ in range(k):
            if not pq:
                break
            val, l, r = heappop(pq)
            ans += -val
            
            # Next best candidate for this left boundary is the next sub-segment to the left
            if r > l:
                next_val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heappush(pq, (-next_val, l, r - 1))
                
        return ans
