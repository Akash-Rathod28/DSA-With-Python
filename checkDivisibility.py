class Solution:

  def checkDivisibility(self, n: int) -> bool:
    sum1 = 0
    mul1 = 1
    for i in str(n):
      d = int(i)
      sum1 += d
      mul1 *= d

    return n % (sum1 + mul1) == 0
