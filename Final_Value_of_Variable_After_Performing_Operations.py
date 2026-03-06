class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for i in operations:
            if i == "++X" or i == "X++":
                a = 1
                x += a
            elif i == "--X" or i == "X--":
                b = -1
                x += b
        return x

        
