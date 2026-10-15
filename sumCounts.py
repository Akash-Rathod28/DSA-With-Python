from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        
        # Segment tree nodes
        sum_sq = [0] * (4 * n)
        sum_val = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_up(node: int):
            left, right = 2 * node, 2 * node + 1
            sum_sq[node] = (sum_sq[left] + sum_sq[right]) % MOD
            sum_val[node] = (sum_val[left] + sum_val[right]) % MOD
            
        def apply(node: int, l: int, r: int, val: int):
            length = r - l + 1
            val %= MOD
            # (f + v)^2 = f^2 + 2*v*f + v^2
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val % MOD * length) % MOD
            sum_val[node] = (sum_val[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push_down(node: int, l: int, r: int):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node: int, l: int, r: int, ql: int, qr: int, val: int):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            push_up(node)

        last_pos = {}
        total_ans = 0
        
        for j, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            # Add 1 to f(i) for all i in [prev + 1, j]
            update(1, 0, n - 1, prev + 1, j, 1)
            last_pos[x] = j
            total_ans = (total_ans + sum_sq[1]) % MOD
            
        return total_ans
