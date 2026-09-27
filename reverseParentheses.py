class Solution:

  def reverseParentheses(self, s: str) -> str:
    stack = []
    for char in s:
      if char == ")":
        # Extract characters inside the parentheses
        current = []
        while stack and stack[-1] != "(":
          current.append(stack.pop())
        # Remove the opening parenthesis '('
        if stack and stack[-1] == "(":
          stack.pop()
        # Push the reversed characters back onto the stack
        stack.extend(current)
      else:
        stack.append(char)

    return "".join(stack)
