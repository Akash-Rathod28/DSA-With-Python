class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        a = len(nums1)
        if a % 2 == 1:   # odd length
            return nums1[a // 2]
        else:            # even length
            return (nums1[a//2 - 1] + nums1[a//2]) / 2
        
