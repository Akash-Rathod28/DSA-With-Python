class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(target - s) < abs(target - closest):
                    closest = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s

        return closest
