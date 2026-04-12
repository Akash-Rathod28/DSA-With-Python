import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse= True)
        # return nums[k-1]

        # nums.sort()
        # return nums[-k]

        h = []
        for x in nums:
            heapq.heappush(h,x)
            if len(h)>k:
                heapq.heappop(h)
        # return h[0]

        return heapq.nlargest(k,h)[-1]

        
