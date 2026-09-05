# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         # if len(nums) == 1:
#         #     return k
#         minimum = []
#         for i in range(len(nums)):
#             minimum.append(max(nums) - min(nums[i:]))
#         a = min(minimum)
#         if a <= k:
#             return minimum.index(a)
#         else:
#             return -1

# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         for i in range(len(nums)):
#             if max(nums[: i + 1]) - min(nums[i:]) <= k:
#                 return i
#         return -1

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        # Precompute suffix minimums: suffix_min[i] = min(nums[i:])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Track prefix maximum on the fly and check condition
        prefix_max = float("-inf")
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
