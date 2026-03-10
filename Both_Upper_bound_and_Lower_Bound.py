class Solution:
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
    def UpperBound(self,nums,target):
        n = len(nums)
        l = 0
        r = n - 1
        ans = n
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if target not in nums:
        #     return [-1,-1]
        
        # a = []
        # for i in range(0, len(nums)):
        #     if nums[i] == target:
        #         a.append(i)
        
        # return [a[0], a[-1]]

        lb = self.LowerBound(nums,target)
        ub = self.UpperBound(nums,target)

        if ub == lb:
            return [-1,-1]
        else:
            return [lb,ub-1]
