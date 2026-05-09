class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        maxi = max(a,b)
        nums = []
        for i in range(1,maxi+1):
            if a % i == 0 and b % i == 0:
                nums.append(i)
        return len(nums)
