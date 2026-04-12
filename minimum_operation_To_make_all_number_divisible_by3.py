class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] % 3 != 0:
        #         count += min(nums[i] % 3, 3 - (nums[i] % 3))
        # return count
        
        count = 0
        for i in nums:
            if i % 3:
                count+=1
        return count
