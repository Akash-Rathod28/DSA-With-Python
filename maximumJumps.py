# class Solution:
#     def maximumJumps(self, nums: List[int], target: int) -> int:
#         if target == 0:
#             return -1
#         n = len(nums)
#         output = 0
#         i,j = 0,1
#         while j <= n - 1:
#             if -target <= (nums[j] - nums[i]) <= target:
#                 output += 1
#             i += 1
#             j += 1
#         return output
            
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == -1:
                continue

            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]
