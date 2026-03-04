class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        s = ""
        for i in range(n):
            s += str(digits[i])
        sum2 = str(int(s) + 1)
        a = []
        for i in sum2:
            a.append(int(i))
        return a


        
        
