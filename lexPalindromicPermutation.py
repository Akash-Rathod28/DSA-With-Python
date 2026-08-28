from collections import Counter


class Solution:

  def lexPalindromicPermutation(self, s: str, target: str) -> str:
    count = Counter(s)
    odd_chars = [c for c, freq in count.items() if freq % 2 != 0]

    if len(odd_chars) > 1:
      return ""

    mid = odd_chars[0] if odd_chars else ""
    half_pool = Counter()
    for c, freq in count.items():
      if freq // 2 > 0:
        half_pool[c] = freq // 2

    n = len(s)
    half_len = n // 2

    def build_palindrome(first_half: list[str]) -> str:
      left = "".join(first_half)
      return left + mid + left[::-1]

    candidates = []

    target_half_count = Counter(target[:half_len])
    if all(target_half_count[c] <= half_pool[c] for c in target_half_count):
      pal = build_palindrome(list(target[:half_len]))
      if pal > target:
        candidates.append(pal)

    prefix_counts = Counter()
    for i in range(half_len):
      for char_code in range(ord(target[i]) + 1, ord("z") + 1):
        c = chr(char_code)
        if half_pool[c] - prefix_counts[c] > 0:
          rem = half_pool - prefix_counts
          rem[c] -= 1
          rem_chars = sorted(rem.elements())
          first_half = list(target[:i]) + [c] + rem_chars
          candidates.append(build_palindrome(first_half))
          break

      prefix_counts[target[i]] += 1
      if prefix_counts[target[i]] > half_pool[target[i]]:
        break

    return min(candidates) if candidates else ""
