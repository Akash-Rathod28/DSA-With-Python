import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = math.gcd(x, mx)
            
        prefix_gcd.sort()
        
        total_sum = 0
        for i in range(n // 2):
            total_sum += math.gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
            
        return total_sum
