from typing import List
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        n = len(self.bit)
        while i < n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = max(q[1] for q in queries)

        obstacles = set()
        coords = {0, mx}

        for q in queries:
            coords.add(q[1])
            if q[0] == 1:
                obstacles.add(q[1])

        coords = sorted(coords)
        idx = {x: i for i, x in enumerate(coords)}

        s = SortedList([0, mx])
        for x in obstacles:
            s.add(x)

        bit = Fenwick(len(coords))

        prev = s[0]
        for i in range(1, len(s)):
            cur = s[i]
            bit.update(idx[cur], cur - prev)
            prev = cur

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                pos = s.index(x)
                left = s[pos - 1]
                right = s[pos + 1]

                bit.update(idx[right], right - left)

                s.remove(x)

            else:
                _, x, sz = q

                pos = s.bisect_right(x) - 1
                left = s[pos]

                best = max(
                    bit.query(idx[left]),
                    x - left
                )

                ans.append(best >= sz)

        return ans[::-1]
