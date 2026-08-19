from collections import defaultdict
from typing import List


class Solution:

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    rows = defaultdict(int)
    for r, c in reservedSeats:
      if 2 <= c <= 9:
        rows[r] |= 1 << (c - 2)

    LEFT_MASK = 0b00001111
    MID_MASK = 0b00111100
    RIGHT_MASK = 0b11110000

    ans = (n - len(rows)) * 2

    for mask in rows.values():
      left_free = (mask & LEFT_MASK) == 0
      right_free = (mask & RIGHT_MASK) == 0
      mid_free = (mask & MID_MASK) == 0

      if left_free and right_free:
        ans += 2
      elif left_free or right_free or mid_free:
        ans += 1

    return ans
