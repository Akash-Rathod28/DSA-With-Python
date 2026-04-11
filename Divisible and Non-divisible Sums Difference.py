class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # divisible_by_m = []
        # not_divisible_by_m = []
        # for i in range(1,n+1):
        #     if i % m == 0:
        #         divisible_by_m.append(i)
        #     else:
        #         not_divisible_by_m.append(i)
        # return sum(not_divisible_by_m) - sum(divisible_by_m)

        count_divisible = 0
        count_not_divisible = 0
        for i in range(1,n+1):
            if i % m == 0:
                count_divisible +=i
            else:
                count_not_divisible += i
        return count_not_divisible - count_divisible
        
