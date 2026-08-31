class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        n = len(vals)
        if n < 3:
            return [-1, -1]

        crit = []
        for i in range(1, n - 1):
            v = vals[i]
            if (v > vals[i - 1] and v > vals[i + 1]) or (v < vals[i - 1] and v < vals[i + 1]):
                crit.append(i)

        if len(crit) < 2:
            return [-1, -1]

        min_d = min(crit[i] - crit[i - 1] for i in range(1, len(crit)))
        max_d = crit[-1] - crit[0]

        return [min_d, max_d]
