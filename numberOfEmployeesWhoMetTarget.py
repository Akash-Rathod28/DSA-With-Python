class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # left = 0
        
        # count = 0
        # while left < len(hours):
        #     if hours[left] >= target:
        #         count += 1
        #         left += 1
        #     else:
        #         left+= 1
        # return count
        
        # count = 0
        # for i in hours:
        #     if i >= target:
        #         count += 1
        # return count

        return sum(h>=target for h in hours)
