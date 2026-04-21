class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = str(n)
        a = a[::-1]
        ab = abs(int(a)-n)
        return ab
        
