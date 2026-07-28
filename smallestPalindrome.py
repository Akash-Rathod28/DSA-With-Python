from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half = []
        mid = ""
        
        for char_code in range(ord('a'), ord('z') + 1):
            ch = chr(char_code)
            if cnt[ch] > 0:
                half.append(ch * (cnt[ch] // 2))
                if cnt[ch] % 2 != 0:
                    mid = ch

        left_half = "".join(half)
        return left_half + mid + left_half[::-1]
