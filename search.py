class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            #return nums.index(target)
            i = 0
            while i < len(nums):
                if nums[i] == target:
                    return i
                else:
                    i += 1
