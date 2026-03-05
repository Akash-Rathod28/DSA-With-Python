# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         sum1 = ""
#         l = []

#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 l = list(s[i:j+1])
                
#                 if l == l[::-1]:   # check palindrome
#                     if len(l) > len(sum1):
#                         sum1 = "".join(l)

#         return sum1


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         sum1 = ""
        
#         for i in range(len(s)):
#             for j in range(i, len(s)):
                
#                 # optimization
#                 if j - i + 1 <= len(sum1):
#                     continue
                
#                 l = s[i:j+1]
                
#                 if l == l[::-1]:
#                     sum1 = l
                        
#         return sum1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):

            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res
