import collections

class Solution:
    MAX_K = 1_000_001

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        odd_count = sum(1 for v in count.values() if v % 2 != 0)
        if odd_count > 1:
            return ""

        half_cnt = [0] * 26
        mid_char = ""
        for char, freq in count.items():
            half_cnt[ord(char) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_char = char

        if self._count_arrangements(half_cnt) < k:
            return ""

        half_len = sum(half_cnt)
        left = []
        for _ in range(half_len):
            for i in range(26):
                if half_cnt[i] == 0:
                    continue
                
                half_cnt[i] -= 1
                ways = self._count_arrangements(half_cnt)
                
                if k <= ways:
                    left.append(chr(ord('a') + i))
                    break
                else:
                    k -= ways
                    half_cnt[i] += 1

        left_str = "".join(left)
        return left_str + mid_char + left_str[::-1]

    def _count_arrangements(self, cnt: list[int]) -> int:
        total = sum(cnt)
        res = 1
        for freq in cnt:
            if freq == 0:
                continue
            res *= self._comb(total, freq)
            if res >= self.MAX_K:
                return self.MAX_K
            total -= freq
        return res

    def _comb(self, n: int, k: int) -> int:
        k = min(k, n - k)
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX_K:
                return self.MAX_K
        return res
