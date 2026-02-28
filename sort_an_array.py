from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # i = 0
        
        # while i < n:
        #     j = 0
        #     while j < n-1:
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]  # swap
        #         j += 1
        #     i += 1
        # return nums

        return sorted(nums)
