class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # li = []
        # max_len = 0
        # for i in range(len(s)):
        #     if s[i] not in li:
        #         li.append(s[i])
        #     else:
        #         if s[i] in li:
        #             max_len = max(len(li),max_len)
                
        #             li.clear()
        #             li.append(s[i])
        # max_len = max(len(li),max_len)
        # return max_len


        n  = len(s)
        if n == 0:
            return 0
        ans = 1
        set1 = set({})
        set1.add(s[0])

        i = 0
        j = 1
        while j < n:
            while s[j] in set1:
                set1.discard(s[i])
                i += 1
            set1.add(s[j])
            j += 1
            ans = max(ans,(j-i))
        return ans
