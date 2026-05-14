class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        while nums:
            a = max(nums)
            b = min(nums)
            nums.remove(a)
            nums.remove(b)
            averages.append((a+b)/2)
        return min(averages)
        
