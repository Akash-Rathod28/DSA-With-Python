class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2 + 1):
            s = str(i)
            for k in range(len(s) - 2):
                if s[k] < s[k+1] and s[k+1] > s[k+2]:
                    count += 1
                if s[k] > s[k+1] and s[k+1] < s[k+2]:
                    count += 1
        return count
