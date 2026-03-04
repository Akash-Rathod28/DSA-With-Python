class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # i = 0
        # while True:
        #     #i = 1
        #     if 3 ** i == n:
        #         return True
            
        #     else:
        #         if 3 ** i > n:
                   
        #             break
        #     i += 1
                
        # return False


        
        if n < 1:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return True
