class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # if dividend == -2**31 and divisor == -1:
        #     return 2**31 - 1
        # a = dividend / divisor
        # return int(a)

        # for positvi number division
        # track = 0
        # count = int(divisor)
        
        # if int(divisor) == 1:
        #     return dividend
        # while True:

        #     if count <= dividend:
        #         count += int(divisor)
        #         track += 1
            
        #     else:
                
        #         return track 

        
        
        
        
        
        # Overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        return sign * result
