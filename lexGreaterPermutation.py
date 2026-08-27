from collections import Counter


class Solution:

  def lexGreaterPermutation(self, s: str, target: str) -> str:
    n = len(s)
    s_count = Counter(s)

    prefix_counts = Counter()
    can_form_prefix = [True] * (n + 1)

    for i, ch in enumerate(target):
      prefix_counts[ch] += 1
      if prefix_counts[ch] > s_count[ch]:
        for j in range(i + 1, n + 1):
          can_form_prefix[j] = False
        break

    for i in range(n - 1, -1, -1):
      if not can_form_prefix[i]:
        continue

      rem = s_count.copy()
      for ch in target[:i]:
        rem[ch] -= 1

      candidates = sorted([ch for ch in rem if rem[ch] > 0 and ch > target[i]])
      if not candidates:
        continue

      best_char = candidates[0]
      rem[best_char] -= 1

      tail = "".join(sorted([ch * count for ch, count in rem.items()]))
      return target[:i] + best_char + tail

    return ""
