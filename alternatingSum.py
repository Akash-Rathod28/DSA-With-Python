class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        if len(nums)==0:
            return nums[0]
        add = nums[0]
        sub = -0
        for i in range(1,len(nums)):
            if i % 2 == 0:
                add += nums[i]
            else:
                sub += nums[i]
        return add - sub
        
        return sum(nums[::2]) - sum(nums[1::2])
                
        
