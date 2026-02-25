class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        v = str(n)
        mul = 1
        su = 0
        for i in v:
            c = int(i)
            mul *=c
            su += c
        return mul - su 
        
