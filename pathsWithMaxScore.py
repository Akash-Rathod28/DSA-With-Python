class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                
                max_score = -1
                paths = 0
                
                for nr, nc in [(r + 1, c), (r, c + 1), (r + 1, c + 1)]:
                    if nr < n and nc < n and dp[nr][nc][1] > 0:
                        next_score, next_paths = dp[nr][nc]
                        
                        if next_score > max_score:
                            max_score = next_score
                            paths = next_paths
                        elif next_score == max_score:
                            paths = (paths + next_paths) % MOD
                
                if max_score != -1:
                    current_val = int(board[r][c]) if board[r][c] != 'E' else 0
                    dp[r][c] = [max_score + current_val, paths]
        
        return dp[0][0]
