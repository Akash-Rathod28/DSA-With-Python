class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        if k == 0:
            return grid
            
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                flat_index = i * n + j
                new_flat_index = (flat_index + k) % total_elements
                new_row = new_flat_index // n
                new_col = new_flat_index % n
                result[new_row][new_col] = grid[i][j]
                
        return result
