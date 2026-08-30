class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        i = nums.index(min(nums))
        j = nums.index(max(nums))

        left = min(i, j)
        right = max(i, j)

        return min(right + 1, n - left, (left + 1) + (n - right))
