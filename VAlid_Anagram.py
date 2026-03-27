class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # return False



        # if len(t) != len(s):
        #     return False
        # for i in s:
        #     if s.count(i) != t.count(i):
        #         return False
        # return True



        
        if len(s) != len(t):
            return False
        
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1
        
        return True
