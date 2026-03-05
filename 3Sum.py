class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums.sort()
        # li = []
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         for k in range(j + 1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if [nums[i],nums[j],nums[k]] not in li:
        #                     li.append([nums[i],nums[j],nums[k]])
        # return li
        
        
        nums.sort()      # Step 1: sort the array
        res = []

        for i in range(len(nums)-2):
            # skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates for second and third numbers
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
