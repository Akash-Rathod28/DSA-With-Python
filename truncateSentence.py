class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        string = ""
        count = 0
        for i in s:
            
            if i != " ":
                string += i
                
            else:
                count += 1
                if count != k:
                    string += " "
            if count == k:
                break
            
        return string


        
