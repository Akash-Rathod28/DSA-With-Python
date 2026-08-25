class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if k not in nums:
            return k
        i = k
        while True:
            if i not in nums:
                return i
            else:
                i += k
