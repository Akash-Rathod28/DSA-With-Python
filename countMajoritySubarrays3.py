class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        tree_size = 2 * n + 2
        bit = [0] * tree_size
        
        def update(idx: int, delta: int):
            while idx < tree_size:
                bit[idx] += delta
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        offset = n + 1
        update(0 + offset, 1)
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
                
            total_subarrays += query(current_sum - 1 + offset)
            update(current_sum + offset, 1)
            
        return total_subarrays
