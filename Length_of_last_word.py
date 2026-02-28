class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
    
        j = len(s) - 1
        length = 0
        
        
        while j >= 0 and s[j] == " ":
            j -= 1
        
        
        while j >= 0 and s[j] != " ":
            length += 1
            j -= 1
        
        return length
                
