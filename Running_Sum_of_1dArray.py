class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # lis = []
        # lis.append(nums[0])
        # i = 1
        # while i < len(nums):
        #     x = lis[i-1] + nums[i]
        #     lis.append(x)
        #     i+=1
        # return lis


        # ans = []
        # ans.append(nums[0])
        # for i in range(1,len(nums)):
        #     x = ans[i-1] + nums[i]
        #     ans.append(x)
        # return ans



        ans = []
        for i in range(1,len(nums) + 1):
           a = sum(nums[:i])
           ans.append(a)
        return ans
