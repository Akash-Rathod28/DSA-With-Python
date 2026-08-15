from functools import reduce
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if not any(nums):
            return 0
        
        total_xor = reduce(lambda x, y: x ^ y, nums, 0)
        
        return len(nums) if total_xor != 0 else len(nums) - 1
