from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Initial quick checks for impossible configurations:
        # 1. Total path length must be even.
        # 2. Starting cell must be '(' and ending cell must be ')'.
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            # Update the balance of parentheses based on the current cell
            k += 1 if grid[i][j] == '(' else -1
            
            # Pruning conditions:
            # 1. If balance drops below 0, we have more ')' than '('.
            # 2. If balance exceeds the remaining steps, we won't be able to balance them out.
            if k < 0 or k > m - i + n - j - 1:
                return False
            
            # Base case: reached the bottom-right corner
            if i == m - 1 and j == n - 1:
                return k == 0
            
            # Explore valid moves (down or right)
            can_move_down = i + 1 < m and dfs(i + 1, j, k)
            can_move_right = j + 1 < n and dfs(i, j + 1, k)
            
            return can_move_down or can_move_right
            
        return dfs(0, 0, 0)
