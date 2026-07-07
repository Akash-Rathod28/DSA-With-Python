class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        sum1 = 0
        sum2 = ""
        for num in str(n):
            if int(num)>0:
                sum2 += num
                sum1 += int(num)
        return sum1*int(sum2)


        
