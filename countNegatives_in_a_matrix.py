class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # count = 0
        # li = []
        # # one method
        # for i in grid:
        #     # for j in range(len(i)):
        #     #     if i[j]<0:
        #     #         count += 1
        #     li += i
        

        # for i in li:
        #     if i < 0:
        #         count += 1
        # return count
        

        return sum(num < 0 for row in grid for num in row)
