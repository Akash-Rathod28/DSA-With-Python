class Solution:
    def mySqrt(self, x: int) -> int:

    # one method
        #return floor(sqrt(x))

    # another method
        if x == 0:
            return 0
        l = 1
        r = x
        ans = 1
        while l <= r:
            mid = (l+r) // 2
            midsquare = mid * mid
            if midsquare > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans
