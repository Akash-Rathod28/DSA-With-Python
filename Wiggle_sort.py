class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        arr = sorted(nums)
        
        mid = (n + 1) // 2
        left = arr[:mid][::-1]
        right = arr[mid:][::-1]
        
        nums[::2] = left
        nums[1::2] = right
