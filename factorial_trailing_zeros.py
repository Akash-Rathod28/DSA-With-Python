class Solution:
    
    def trailingZeroes(self, n: int) -> int:
        # i = 2
        # fact = 1
        # while i <= n:
        #     fact *= i
        #     i += 1
        # count = 0
        # a = str(fact)
        # rev = a[::-1]
        
        
        # for i in rev:
        #     if i  == "0":
        #         count += 1 
        #     elif i != "0":
        #         break
        # return count
        return n//5 + self.trailingZeroes(n//5) if n else 0

        

        
