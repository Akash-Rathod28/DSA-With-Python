import math
from functools import cache
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @cache
        def dp(i: int, g1: int, g2: int) -> int:
            if i == n:
                return 1 if g1 > 0 and g1 == g2 else 0
            
            current_num = nums[i]
            
            res = dp(i + 1, g1, g2)
            
            next_g1 = current_num if g1 == 0 else math.gcd(g1, current_num)
            res = (res + dp(i + 1, next_g1, g2)) % MOD
            
            next_g2 = current_num if g2 == 0 else math.gcd(g2, current_num)
            res = (res + dp(i + 1, g1, next_g2)) % MOD
            
            return res
        
        return dp(0, 0, 0)
