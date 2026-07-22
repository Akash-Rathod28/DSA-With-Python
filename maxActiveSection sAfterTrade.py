from typing import List

class SparseTable:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        if self.n == 0:
            return
        self.k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.k)]
        
        for i in range(self.n):
            self.st[0][i] = arr[i]
            
        for j in range(1, self.k):
            length = 1 << (j - 1)
            for i in range(self.n - (1 << j) + 1):
                self.st[j][i] = max(self.st[j - 1][i], self.st[j - 1][i + length])

    def query(self, L: int, R: int) -> int:
        if L > R:
            return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        zero_groups = []
        zero_group_idx = [-1] * n
        
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    zero_group_idx[i] = len(zero_groups)
                    i += 1
                zero_groups.append({
                    'start': start,
                    'end': i - 1,
                    'length': i - start
                })
            else:
                i += 1
                
        num_groups = len(zero_groups)
        
        if num_groups == 0:
            return [total_ones] * len(queries)

        adj_sums = [
            zero_groups[g]['length'] + zero_groups[g + 1]['length']
            for g in range(num_groups - 1)
        ]
        st = SparseTable(adj_sums)
        
        ans = []
        for l, r in queries:
            first_g = -1
            for k in range(l, r + 1):
                if zero_group_idx[k] != -1:
                    first_g = zero_group_idx[k]
                    break
                    
            if first_g == -1:
                ans.append(total_ones)
                continue
                
            last_g = -1
            for k in range(r, l - 1, -1):
                if zero_group_idx[k] != -1:
                    last_g = zero_group_idx[k]
                    break
                    
            if first_g == last_g:
                ans.append(total_ones)
                continue
                
            first_len = zero_groups[first_g]['end'] - max(l, zero_groups[first_g]['start']) + 1
            last_len = min(r, zero_groups[last_g]['end']) - zero_groups[last_g]['start'] + 1
            
            max_gain = 0
            
            if first_g + 1 == last_g:
                max_gain = first_len + last_len
            else:
                gain1 = first_len + zero_groups[first_g + 1]['length']
                gain2 = zero_groups[last_g - 1]['length'] + last_len
                gain_internal = st.query(first_g + 1, last_g - 2)
                
                max_gain = max(gain1, gain2, gain_internal)
                
            ans.append(total_ones + max_gain)
            
        return ans
