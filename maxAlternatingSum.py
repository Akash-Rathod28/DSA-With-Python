from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 1. Get the square of each number and sort them in ascending order
        squares = sorted([x * x for x in nums])
        
        # 2. Find how many numbers will fall on odd indices (to be subtracted)
        k = len(nums) // 2
        
        # 3. Subtract the smallest 'k' squares, and add the remaining squares
        # squares[:k] are the smallest k elements
        # squares[k:] are the remaining largest elements
        return sum(squares[k:]) - sum(squares[:k])
