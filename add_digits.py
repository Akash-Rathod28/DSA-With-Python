class Solution:
    def addDigits(self, num: int) -> int:
        # if len(str(num)) == 1:
        #     return num
        # while True:
        #     s = str(num)
        #     sum1 = 0
            
        #     for i in range(len(s)):  
        #         sum1 = sum1 + int(s[i])
            
        #     if len(str(sum1)) == 1:  
        #         return sum1
        #     else:
        #         num = sum1    

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
        
