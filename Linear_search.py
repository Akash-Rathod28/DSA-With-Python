class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        # i = 0
        # while i <= len(nums):
        #     if nums[i] == target:
        #         return i
        #     i += 1


        ## USING FOR LOOP
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
