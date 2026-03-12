class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = (rows * columns) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid//columns][mid % columns] == target:
                return True
            elif matrix[mid//columns][mid % columns] > target:
                # left
                r = mid - 1
            else:
                # right
                l = mid + 1
        return False
