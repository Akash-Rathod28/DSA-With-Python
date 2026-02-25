class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        g = []
        a = max(candies)
        for i in candies:
            if (i + extraCandies) >= a:
                g.append(True)
            else:
                g.append(False)
        return g

