from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            counts = Counter(nums)
            unique_elements = [x for x, freq in counts.items() if freq == 1]
            return max(unique_elements) if unique_elements else -1
        if k == n:
            return max(nums)
        counts = Counter(nums)
        candidates = []
        if counts[nums[0]] == 1:
            candidates.append(nums[0])
        if counts[nums[-1]] == 1:
            candidates.append(nums[-1])
        return max(candidates) if candidates else -1
