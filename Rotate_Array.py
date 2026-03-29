class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(1,k+1):
        #     a = nums[-1]
        #     nums.pop()
        #     nums.insert(0,a)

    
        n = len(nums)
        k = k % n   # handle large k
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 
                r -= 1
        
        reverse(0, n - 1)     # step 1
        reverse(0, k - 1)     # step 2
        reverse(k, n - 1)     # step 3


        
