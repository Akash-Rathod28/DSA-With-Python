class Solution:

  def stoneGameV(self, stoneValue: list[int]) -> int:
    n = len(stoneValue)
    if n <= 1:
      return 0

    pref = [0] * (n + 1)
    for i in range(n):
      pref[i + 1] = pref[i] + stoneValue[i]

    dp = [[0] * n for _ in range(n)]
    maxL = [[0] * n for _ in range(n)]
    maxR = [[0] * n for _ in range(n)]

    for i in range(n):
      maxL[i][i] = stoneValue[i]
      maxR[i][i] = stoneValue[i]

    for length in range(2, n + 1):
      k = 0
      for i in range(n - length + 1):
        j = i + length - 1

        if k < i:
          k = i
        total_sum = pref[j + 1] - pref[i]

        while k < j and (pref[k + 1] - pref[i]) * 2 <= total_sum:
          k += 1

        best = 0
        left_k = k - 1

        if left_k >= i:
          best = max(best, maxL[i][left_k])

        if (
            left_k >= i
            and (pref[left_k + 1] - pref[i]) * 2 == total_sum
            and left_k + 1 <= j
        ):
          best = max(best, maxR[left_k + 1][j])

        if k < j:
          best = max(best, maxR[k + 1][j])

        dp[i][j] = best
        maxL[i][j] = max(maxL[i][j - 1], dp[i][j] + total_sum)
        maxR[i][j] = max(maxR[i + 1][j], dp[i][j] + total_sum)

    return dp[0][n - 1]
