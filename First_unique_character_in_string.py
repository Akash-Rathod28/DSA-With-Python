class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in s:
        #     if s.count(i) ==1:
        #         return s.index(i)
        # else:
        #     return -1
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
