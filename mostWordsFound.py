class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        li = []
        for i in s:
            count = 0
            for j in i:
                if j == " ":
                    count+=1
            li.append(count +1)
            
        return max(li)
