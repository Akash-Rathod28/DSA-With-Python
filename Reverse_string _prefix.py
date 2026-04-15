class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # s1 = ""
        # s1 += s[0:k]
        # a = s1[::-1]
        # a += s[k:]

        # return a
        # a = "" 
        # for u,i in enumerate(s):
        #     if u < k:
        #         a += i
        # a = a[::-1]
        # for i in range(k,len(s)):
        #     a += s[i]
        # return a

        # return s[:k][::-1] + s[k:]

        s = list(s)
        i, j = 0, k - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
