class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for val in patterns:
            if val in word:
                count += 1
        return count
                        
        
