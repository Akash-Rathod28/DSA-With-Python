class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # if len(s) < 3:
        #     return 0
        
        # n = len(s) - 3
        # count = 0
        # i = 0
        
        # while i <= n:
        #     a = s[i] + s[i+1] + s[i+2]
            
        #     if a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        #         count += 1
                
        #     i += 1
        
        # return count

        #---> another method
        # count = 0
        # for i in range(0,len(s)-2):
        #     a = s[i] + s[i+1] + s[i+2]
        #     if len(a) == len(set(a)):
        #         count+=1
        # return count
    
        # ---> another method
        count = 0
        for i in range(0,len(s)-2):
            a = s[i] + s[i+1] + s[i+2]
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
                count += 1
        return count
