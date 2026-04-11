class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        st = 0
        while st < len(stones):
            if stones[st] in jewels:
                count += 1
            st += 1
        return count

        
