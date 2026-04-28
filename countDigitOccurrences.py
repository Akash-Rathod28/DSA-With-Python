class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # output = 0
        # for i in nums:
            
        #         for j in str(i):
        #             if int(j) == digit:
        #                 output += 1
        # return output
        count = 0
        right = 0
        while right < len(nums):
            for i in str(nums[right]):
                if i == str(digit):
                    count += 1
            right+=1
        return count

