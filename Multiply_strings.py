class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1

                s = mul + res[p2]

                res[p2] = s % 10
                res[p1] += s // 10

        result = "".join(map(str, res)).lstrip("0")
        return result if result else "0"
