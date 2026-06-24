class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:
            return r - l + 1
        
        MOD = 10**9 + 7
        k = r - l + 1
        if k <= 1:
            return 0
            
        size = 2 * k
        T = [[0] * size for _ in range(size)]
        
        for x in range(k):
            for y in range(x + 1, k):
                T[y][x + k] = 1
            for y in range(x):
                T[y + k][x] = 1
                
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k_idx in range(size):
                    if A[i][k_idx] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k_idx] * B[k_idx][j]) % MOD
            return C

        def power(base, exp):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            while exp > 0:
                if exp & 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                exp >>= 1
            return res

        T_pow = power(T, n - 1)
        
        ans = 0
        for i in range(size):
            s = 0
            for j in range(size):
                s = (s + T_pow[i][j]) % MOD
            ans = (ans + s) % MOD
            
        return ans
