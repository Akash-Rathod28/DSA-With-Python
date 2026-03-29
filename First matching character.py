class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return -1
        
        
        for i in range(n):                   
            if s[i] == s[n-i-1]:            
                return i                    
        return -1    


       
