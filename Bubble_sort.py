class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
# #---> USING BUBBLE SORT:::::
        n = len(nums)
        for i in range(n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    isSwap = True
            if not isSwap:
                break
        return nums
