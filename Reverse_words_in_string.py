class Solution:
    def reverseWords(self, s: str) -> str:
        #a = s.strip()
        #return " ".join(s.split()[::-1])
        s = s.strip()
        s = s.split() # it converts string into list
        
        s.reverse()
        return " ".join(s)
        
