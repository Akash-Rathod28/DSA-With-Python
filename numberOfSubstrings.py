class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_pos[char] = i
            count += min(last_pos.values()) + 1
                
        return count
