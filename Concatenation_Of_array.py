class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # li = []
        # ans = nums.copy()
        # li.extend(nums)
        # li.extend(ans)
        # return li

    ### _____ >>>> another method
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(nums[i])
        # for i in range(len(nums)):
        #     ans.append(nums[i])
        # return ans

    ### _____ >>>> another method
        # return nums +  nums

    ### _____ >>>> another method
        # return nums *2

    ### _____ >>>> another method
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        
        
