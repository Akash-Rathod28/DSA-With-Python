from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        sum_d = [0] * (n + 1)
        cnt_n0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        for i in range(n):
            d = int(s[i])
            sum_d[i + 1] = sum_d[i] + d
            if d > 0:
                cnt_n0[i + 1] = cnt_n0[i] + 1
                p[i + 1] = (p[i] * 10 + d) % MOD
            else:
                cnt_n0[i + 1] = cnt_n0[i]
                p[i + 1] = p[i]
                
        output = []
        for a, b in queries:
            current_sum = sum_d[b + 1] - sum_d[a]
            
            num_non_zeros =cnt_n0[b + 1] - cnt_n0[a]
            
            current_val = (p[b + 1] - p[a] * pow10[num_non_zeros]) % MOD
            
            output.append((current_val * current_sum) % MOD)
            
        return output
