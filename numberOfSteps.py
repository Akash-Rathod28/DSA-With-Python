class Solution:
    def numberOfSteps(self, num: int) -> int:
        output = []
        
        while num != 0:
            # if num == 0:
            #     break
            if num % 2 == 0:
                num //= 2
                output.append(num)
            else:
                num -= 1
                output.append(num)
        return len(output)
            
        
        
