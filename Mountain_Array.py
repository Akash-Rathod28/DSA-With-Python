class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        # b = max(arr)
        # return arr.index(b)

        n = len(nums)
        l = 0
        r = n - 2

        ans = n - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid+1]:
                #right
                l = mid + 1
            else:
                ans = mid
                # left
                r = mid - 1
        return ans
