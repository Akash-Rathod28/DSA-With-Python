class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        b = list(set(word))
        count = 0
        for i in b:
            if i.islower():
               
                a = i.capitalize()
                if a in b:
                    count += 1
        return count
