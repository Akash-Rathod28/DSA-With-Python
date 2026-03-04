class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            if i * i == num:
                return True
            elif i * i > num:
                break
            i += 1
        return False
