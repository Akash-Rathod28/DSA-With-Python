class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # res = 0
        # for i in nums:
        #     a = nums.count(i)
        #     if a == 1:
        #         res = i
        #         break
        # return res


        # USING XOR
        res = 0
        for num in nums:
            res ^= num   # XOR each number
        return res
