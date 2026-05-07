class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        for i in nums:
            sum1 += i

        sum2 = 0
        for i in nums:
            stirng = str(i)
            for j in stirng:
                sum2 += int(j)
        
        return abs(sum1-sum2)

        
