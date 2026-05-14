class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        exepected = list(range(1,n+1))
        exepected.append(n)
        return sorted(nums) == exepected
        
