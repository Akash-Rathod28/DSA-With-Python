from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        sample = "123456789"
        n = len(sample)
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length + 1):
                substring = sample[start : start + length]
                num = int(substring)
                
                if low <= num <= high:
                    result.append(num)
                    
        return result
