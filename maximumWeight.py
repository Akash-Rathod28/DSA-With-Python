import bisect
import functools
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class T:
  weight: int
  selected: tuple[int]


class Solution:

  def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
    # Attach original indices and sort by start time
    intervals = sorted((*interval, i) for i, interval in enumerate(intervals))

    @functools.lru_cache(None)
    def dp(i: int, quota: int) -> T:
      if i == len(intervals) or quota == 0:
        return T(0, ())

      # Option 1: Skip current interval
      skip = dp(i + 1, quota)

      # Option 2: Pick current interval
      _, r, weight, originalIndex = intervals[i]
      # Find the first interval starting strictly after current interval's end time 'r'
      j = bisect.bisect_right(intervals, (r, math.inf))
      nextRes = dp(j, quota - 1)
      pick = T(
          weight + nextRes.weight, sorted((originalIndex, *nextRes.selected))
      )

      # Return the better choice (maximize weight, then lexicographically smallest indices)
      if pick.weight > skip.weight or (
          pick.weight == skip.weight and pick.selected < skip.selected
      ):
        return pick
      return skip

    return list(dp(0, 4).selected)
