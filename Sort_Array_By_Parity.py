class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    # one method
        # a = []
        # for i in nums:
        #     if i % 2 ==0:
        #         a.append(i)
        # for i in nums:
        #     if i % 2 != 0:
        #         a.append(i)
        # return a

    # another method
        start = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[start],nums[i] = nums[i],nums[start]
                start += 1
        return nums
