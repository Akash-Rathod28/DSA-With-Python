from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(N: int) -> int:
            if N < 100: 
                return 0
            
            s = str(N)
            n = len(s)
            
            @lru_cache(None)
            def dp(idx, prev, prev2, is_less, is_started):
                # Base Case: When we reach the end, we have successfully formed exactly 1 valid number
                if idx == n:
                    return 0, 1
                
                limit = 9 if is_less else int(s[idx])
                total_waviness = 0
                total_ways = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            # Still processing leading zeros
                            sub_waviness, sub_ways = dp(idx + 1, -1, -1, next_less, False)
                        else:
                            # Placed the first non-zero digit
                            sub_waviness, sub_ways = dp(idx + 1, d, -1, next_less, True)
                    else:
                        # Checking if the PREVIOUS digit 'prev' forms a peak or valley
                        is_wave = 0
                        if prev2 != -1:
                            if prev2 < prev > d:    # Peak
                                is_wave = 1
                            elif prev2 > prev < d:  # Valley
                                is_wave = 1
                        
                        sub_waviness, sub_ways = dp(idx + 1, d, prev, next_less, True)
                        
                        # If a wave point was found at 'prev', it contributes 1 
                        # to all 'sub_ways' combinations that follow it.
                        total_waviness += (is_wave * sub_ways)
                    
                    total_waviness += sub_waviness
                    total_ways += sub_ways
                        
                return total_waviness, total_ways
            
            # The function returns a tuple: (total_waviness, total_ways)
            return dp(0, -1, -1, False, False)[0]

        return solve(num2) - solve(num1 - 1)
