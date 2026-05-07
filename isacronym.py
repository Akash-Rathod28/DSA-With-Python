class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) == len(words):
            for i in range(len(words)): 
                if s[i] not in words[i][0]:
                    return False
            return True    
        return False   

       
