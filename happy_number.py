class Solution:
    def isHappy(self, n: int) -> bool:
        # a = str(n)
        # if a == "1":
        #     return True
        # if len(a) <= 1:
        #     return False
        
        # while True:
        #     if len(a) >=2:
        #         b = []
        #         g = list(a)
        #         if len(b) != 1:
        #             for i in g:
        #                 c = int(i)
        #                 b.append(c*c)
        #                 g = sum(b)
        #     if len(b) == 1:
        #         return True
        #     else:
        #         return False
        seen = set()
        while True:
            if n == 1:
                return True
            
            if n in seen:
                return False
            
            seen.add(n)
            
            a = str(n)
            b = []
            
            for i in a:
                c = int(i)
                b.append(c * c)
            
            n = sum(b)

        
