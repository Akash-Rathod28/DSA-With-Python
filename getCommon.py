class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # li = []
        # for i in nums1:
        #     if i in nums2:
        #         li.append(i)
        # return min(li)

        # a = set(nums1).intersection(set(nums2))
        # return min(a)

        # for i in range(len(nums1)):
        #     if min(nums2) in nums1:
        #         return min(nums2)
        #     else:
        #         nums2.pop(0)

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                return nums1[i]

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return -1
