class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, it's not the outermost '('
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                # If depth > 0 after decrementing, it's not the outermost ')'
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)
