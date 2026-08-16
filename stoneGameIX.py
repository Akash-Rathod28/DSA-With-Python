from collections import Counter
from typing import List


class Solution:

  def stoneGameIX(self, stones: List[int]) -> bool:
    count = Counter(x % 3 for x in stones)
    c0, c1, c2 = count[0], count[1], count[2]

    if c0 % 2 == 0:
      return c1 >= 1 and c2 >= 1
    else:
      return abs(c1 - c2) > 2
