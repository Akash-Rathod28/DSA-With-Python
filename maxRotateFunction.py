class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # rotate = 0
        # le = []

        # while rotate < len(nums):
        #     count = 0
        #     for idx,val in enumerate(nums):
        #         count += idx * val
        #     le.append(count)
        #     nums = [nums[-1]] + nums[:-1]
        #     rotate += 1
        # return max(le)

        


        # count = []
        # for _ in range(len(nums)):  # rotate 1 time
        #     nums = [nums[-1]] + nums[:-1]
        #     count1 = 0
        #     for idx,val in enumerate(nums):
        #         count1 += idx* val
        #     count.append(count1)
        # return max(count)



        n = len(nums)

        totalsum = sum(nums) 

        f = sum(i * num for i,num in enumerate(nums))

        max_val = f
        for k in range(1,n):
            f = f + totalsum - n * nums[-k]
            max_val = max(max_val,f)
        return max_val
