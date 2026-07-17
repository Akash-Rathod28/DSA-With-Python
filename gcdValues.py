import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        multiples = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                multiples[i] += counts[j]
                
        gcd_pairs = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            c = multiples[i]
            total_pairs = c * (c - 1) // 2
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= gcd_pairs[j]
            gcd_pairs[i] = total_pairs
            
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + gcd_pairs[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans
