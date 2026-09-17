class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        ans = float('inf')
        
        sum_val = 0
        l = 0
        
        for r in range(n):
            sum_val += arr[r]
            
            while sum_val > target:
                sum_val -= arr[l]
                l += 1
                
            if sum_val == target:
                if l > 0 and best[l - 1] != float('inf'):
                    ans = min(ans, best[l - 1] + (r - l + 1))
                best[r] = r - l + 1
                
            if r > 0:
                best[r] = min(best[r], best[r - 1])
                
        return ans if ans != float('inf') else -1
