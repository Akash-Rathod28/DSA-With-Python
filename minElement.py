class Solution:
    def minElement(self, nums: List[int]) -> int:
        for idx,i in enumerate(nums):
            count = 0
            if i >= 10:
                for j in str(i):
                    count += int(j)
            else:
                count += i
            nums[idx] = count
        return min(nums)
            

        
