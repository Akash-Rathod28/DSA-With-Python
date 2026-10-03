class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the opening bracket onto the stack
                stack.append(i)
            else:
                # Pop the top element (matching '(' or the base boundary)
                stack.pop()
                
                # If the stack is empty, it means this ')' doesn't have a match.
                # Push the current index as the new base boundary.
                if not stack:
                    stack.append(i)
                else:
                    # Otherwise, the length of the valid substring is the current index 
                    # minus the index at the top of the stack.
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
