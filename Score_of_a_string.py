class Solution:
    def scoreOfString(self, s: str) -> int:
        # if len(s) == 1:
        #     return ord(s)
        # result = []
        # for i in s:
        #     result.append(ord(i))
        # add = []
        # for i in range(len(result)-1):
        #     a = abs(result[i] - result[i+1])
        #     add.append(a)
        
        # return sum(add)
            

        total = 0
        for i in range(len(s)-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total
