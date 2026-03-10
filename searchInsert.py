class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
        # ans = 0
        # a = len(nums)
        # if target in nums:
        #     for i in range(0,len(nums)):
        #         if nums[i] == target:
        #             return i
        # else:
        #     for i in range(0,len(nums)):
        #         if nums[i] >= target + 1:
        #             return i
        
        # return a


        ##USING BINARY SEARCH and lower bound
    def LowerBound(self,nums,target):
        n = len(nums)
        l = 0
        r = n - 1
        ans = n
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.LowerBound(nums,target)
        
