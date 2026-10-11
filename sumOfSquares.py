class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through the array using a 0-based index
        for i in range(n):
            # Convert to 1-based index by using (i + 1)
            if n % (i + 1) == 0:
                total_sum += nums[i] ** 2
                
        return total_sum
