class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 32
        
        # Step 1: Count the total number of 1s at each bit position
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    counts[i] += 1
                    
        ans = 0
        
        # Step 2 & 3: Construct the k largest possible numbers and sum their squares
        for _ in range(k):
            current_num = 0
            for i in range(32):
                # If we have a '1' available at this bit position, use it
                if counts[i] > 0:
                    current_num |= (1 << i)
                    counts[i] -= 1
            
            # Square the constructed number and add to our total modulo 10^9 + 7
            ans = (ans + current_num * current_num) % MOD
            
        return ans
