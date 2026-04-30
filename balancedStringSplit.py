class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # count = 0
        # r_count = 0
        # l_count = 0
        # for i in s:
            
            
        #     if i == "L":
        #         l_count += 1
        #     elif i == "R":
        #         r_count += 1
        #     if r_count == l_count:
        #         count += 1
        #         r_count = 0
        #         l_count = 0
        # return count

        count = 0
        balance = 0
        for i in s:
            if i == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
