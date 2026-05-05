class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # if len(matrix) == 1:
        #     return [0]
        # output = []
        # for i in range(len(matrix)):
        #     count1 = 0
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 1:
        #             count1 += 1
        #     if count1 >= 1:
        #         output.append(count1)
        #     else:
        #         output.append(0)
        # return output

        
        return [row.count(1) for row in matrix]


        
