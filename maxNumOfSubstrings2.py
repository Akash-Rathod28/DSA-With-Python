class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [0] * 26
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = i
            
        res = []
        r = -1
        
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if i != left[char_idx]:
                continue
                
            new_r = right[char_idx]
            j = i + 1
            valid = True
            
            while j <= new_r:
                curr_idx = ord(s[j]) - ord('a')
                if left[curr_idx] < i:
                    valid = False
                    break
                new_r = max(new_r, right[curr_idx])
                j += 1
                
            if valid:
                if i > r:
                    res.append(s[i:new_r + 1])
                else:
                    res[-1] = s[i:new_r + 1]
                r = new_r
                
        return res
