class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        li = []
        for idx,val in enumerate(nums):
            if val % 2 == 0:
                nums[idx] = 0
            else:
                nums[idx] = 1
        nums.sort()
        return nums
        
