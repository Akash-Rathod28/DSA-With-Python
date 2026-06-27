import collections

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_num = max(nums)
        
        if 1 in count:
            ans = count[1] - (1 if count[1] % 2 == 0 else 0)
        else:
            ans = 1
            
        for num in count:
            if num == 1:
                continue
                
            length = 0
            x = num
            
            while x <= max_num and x in count and count[x] >= 2:
                length += 2
                x *= x
            
            if x in count and count[x] >= 1:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length - 1)
                
        return ans
