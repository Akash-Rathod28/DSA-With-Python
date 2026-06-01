# class Solution:
#     def minimumCost(self, cost: List[int]) -> int:
#         return sum(val for idx, val in enumerate(sorted(cost, reverse = True)) if idx % 3 != 2)

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        # Delete every 3rd element starting from index 2
        del cost[2::3] 
        return sum(cost)
