# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums.sort()
#         a = set(nums)
#         nums = list(a)
#         if 1 not in nums:
#                 return 1
#         for i in range(len(nums)-1):
            
#             if nums[i] < 0:
#                 continue
#             elif nums[i] + 1 == nums[i+1]:
#                 continue
#             elif nums[i] + 1 != nums[i+1]:
#                 return nums[i] + 1
#         return nums[-1] + 1



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))   # remove duplicates + sort
        
        # if 1 not in nums:
        #     return 1
        
        # for i in range(len(nums) - 1):
        #     if nums[i] <= 0:
        #         continue
        #     elif nums[i + 1] != nums[i] + 1:
        #         return nums[i] + 1        
        # return nums[-1] + 1
            

        
        nums_set = set(nums)   # O(n)

        i = 1
        while True:
            if i not in nums_set:
                return i
            i += 1
