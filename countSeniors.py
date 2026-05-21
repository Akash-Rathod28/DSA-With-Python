class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            a = details[i][11:13]
            
            if int(a)>60:
                count += 1
        return count

        
