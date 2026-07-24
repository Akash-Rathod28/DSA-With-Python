from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairwise_xors = {a ^ b for i, a in enumerate(nums) for b in nums[i:]}
        triplet_xors = {pair_xor ^ x for pair_xor in pairwise_xors for x in nums}
        return len(triplet_xors)
