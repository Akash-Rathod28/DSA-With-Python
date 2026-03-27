class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
            if curr_sum < 0 :
                curr_sum = 0
        return max_sum



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
