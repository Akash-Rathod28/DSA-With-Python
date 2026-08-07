import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"

        n = len(num)

        def min_digits_needed(target: int) -> int:
            if target == 1:
                return 0
            c2, c3, c5, c7 = 0, 0, 0, 0
            temp = target
            while temp % 2 == 0: temp //= 2; c2 += 1
            while temp % 3 == 0: temp //= 3; c3 += 1
            while temp % 5 == 0: temp //= 5; c5 += 1
            while temp % 7 == 0: temp //= 7; c7 += 1
            count9 = c3 // 2
            c3 %= 2
            count8 = c2 // 3
            c2 %= 3
            count6 = 1 if (c2 > 0 and c3 > 0) else 0
            if count6:
                c2 -= 1
                c3 -= 1
            count4 = c2 // 2
            c2 %= 2
            return count9 + count8 + count6 + count4 + c2 + c3 + c5 + c7

        def get_smallest_with_len(length: int, target: int) -> str:
            res = []
            curr = target
            for pos in range(length):
                rem_len = length - 1 - pos
                for d in range(1, 10):
                    next_curr = curr // math.gcd(curr, d)
                    if min_digits_needed(next_curr) <= rem_len:
                        res.append(str(d))
                        curr = next_curr
                        break
            return "".join(res) if curr == 1 else ""

        digits = [0] * n

        def dfs(idx: int, is_greater: bool, req_t: int) -> bool:
            if req_t == 1 and is_greater:
                for i in range(idx, n):
                    digits[i] = 1
                return True
            if idx == n:
                return req_t == 1

            rem_len = n - idx
            if min_digits_needed(req_t) > rem_len:
                return False

            start_digit = 1 if is_greater else max(1, int(num[idx]))

            for d in range(start_digit, 10):
                digits[idx] = d
                next_t = req_t // math.gcd(req_t, d)
                if dfs(idx + 1, is_greater or (d > int(num[idx])), next_t):
                    return True

            return False

        if dfs(0, False, t):
            return "".join(map(str, digits))

        length = n + 1
        while True:
            if min_digits_needed(t) <= length:
                candidate = get_smallest_with_len(length, t)
                if candidate:
                    return candidate
            length += 1
