class SegmentTreeNode:
    def __init__(self, k):
        self.prod = 1
        self.remain = [0] * k

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        nums = [x % k for x in nums]
        tree = [SegmentTreeNode(k) for _ in range(4 * n)]
        
        def merge(left_node, right_node):
            res = SegmentTreeNode(k)
            res.prod = (left_node.prod * right_node.prod) % k
            for i in range(k):
                res.remain[i] = left_node.remain[i]
            for i in range(k):
                new_rem = (left_node.prod * i) % k
                res.remain[new_rem] += right_node.remain[i]
            return res

        def build(node, l, r):
            if l == r:
                tree[node].prod = nums[l]
                tree[node].remain[nums[l]] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, l, r, idx, val):
            if l == r:
                tree[node].prod = val
                tree[node].remain = [0] * k
                tree[node].remain[val] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            elif ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
            else:
                return merge(query(2 * node, l, mid, ql, mid), 
                             query(2 * node + 1, mid + 1, r, mid + 1, qr))

        build(1, 0, n - 1)
        ans = []
        
        for idx, val, start, xi in queries:
            val_mod = val % k
            nums[idx] = val_mod
            update(1, 0, n - 1, idx, val_mod)
            
            # Query the suffix starting from `start` up to `n - 1`
            res_node = query(1, 0, n - 1, start, n - 1)
            ans.append(res_node.remain[xi])
            
        return ans
