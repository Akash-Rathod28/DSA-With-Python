class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped character doesn't match the stack's top element, return False
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack
