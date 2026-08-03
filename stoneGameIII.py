from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp1 = dp2 = dp3 = 0

        for i in range(n - 1, -1, -1):
            take = 0
            best = float('-inf')
            for k in range(1, 4):
                if i + k - 1 < n:
                    take += stoneValue[i + k - 1]
                    next_dp = dp1 if k == 1 else (dp2 if k == 2 else dp3)
                    best = max(best, take - next_dp)
            dp1, dp2, dp3 = best, dp1, dp2

        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"
