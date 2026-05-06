class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) == len(words):
            for i in range(len(words)): 
                if s[i] in words[i]:
                    continue
                else:
                    return False
        return False      
            
