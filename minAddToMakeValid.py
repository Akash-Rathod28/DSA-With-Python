class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0  # Tracks unmatched opening parentheses
        ans = 0  # Tracks required insertions
        
        for c in s:
            if c == '(':
                bal += 1
            else:  # c == ')'
                if bal > 0:
                    bal -= 1
                else:
                    ans += 1
                    
        return ans + bal
