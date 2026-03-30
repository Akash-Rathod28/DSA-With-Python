class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        
        
        for a in nums1:
            for b in nums2:
                s = a + b
                hashmap[s] = hashmap.get(s, 0) + 1
        
        count = 0
        
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in hashmap:
                    count += hashmap[target]
        
        return count
