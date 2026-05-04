class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        


        # res = [[0]*len(matrix) for _ in range(len(matrix))]
        # n = len(matrix[0])
        # for i in range(n):
        #     num1 = []
        #     for j in range(n):
        #         num1.append(matrix[j][i])
        #     num1.reverse()
        #     res[i] = num1
        # for i in range(len(matrix)):
        #     matrix[i] = res[i]

        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):   # start from i (important)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

        
        
