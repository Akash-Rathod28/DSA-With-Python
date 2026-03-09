# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         ret = []
#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     for l in range(k+1, n):
#                         a = nums[i] + nums[j] + nums[k] + nums[l]
#                         if a == target:
#                             quad = [nums[i], nums[j], nums[k], nums[l]]
#                             quad.sort()
#                             if quad not in ret:
#                                 ret.append(quad)

#         return ret




class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return res
