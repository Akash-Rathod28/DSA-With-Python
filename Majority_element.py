class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)//2
        # for num in nums:
        #     if nums.count(num) > n:
        #         return num
        num = None
        count = 0
        for i in nums:
            if count == 0:
                num = i
            if i == num:
                count += 1
            else:
                count -= 1
        return num
