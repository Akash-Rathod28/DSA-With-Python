from bisect import bisect_left
from typing import List


class Solution:

  def validSequence(self, word1: str, word2: str) -> List[int]:
    n, m = len(word1), len(word2)

    pos = [[] for _ in range(26)]
    for i, ch in enumerate(word1):
      pos[ord(ch) - 97].append(i)

    def get_prev(ch_code: int, target: int) -> int:
      lst = pos[ch_code]
      idx = bisect_left(lst, target) - 1
      return lst[idx] if idx >= 0 else -1

    last = [-1] * (m + 1)
    last[m] = n
    for i in range(m - 1, -1, -1):
      last[i] = get_prev(ord(word2[i]) - 97, last[i + 1])

    last1 = [-1] * (m + 1)
    last1[m] = n
    for i in range(m - 1, -1, -1):
      c_code = ord(word2[i]) - 97
      op1 = last[i]
      op2 = last[i + 1] - 1 if last[i + 1] > 0 else -1
      op3 = get_prev(c_code, last1[i + 1])
      last1[i] = max(op1, op2, op3)

    if last1[0] < 0:
      return []

    ans = []
    curr_j = 0
    changed = False

    for i in range(m):
      c_code = ord(word2[i]) - 97

      lst = pos[c_code]
      idx = bisect_left(lst, curr_j)
      match_j = lst[idx] if idx < len(lst) else -1

      can_mismatch = not changed and curr_j < n and last[i + 1] > curr_j

      chosen_j = -1
      use_change = False

      if can_mismatch and (match_j == -1 or curr_j < match_j):
        chosen_j = curr_j
        use_change = True
      elif match_j != -1:
        req_last = last[i + 1] if changed else last1[i + 1]
        if req_last > match_j:
          chosen_j = match_j
          use_change = False

      if chosen_j == -1:
        return []

      ans.append(chosen_j)
      if use_change:
        changed = True
      curr_j = chosen_j + 1

    return ans
