class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for string in s:
            if string.isdigit():
                stack.pop()
            else:
                stack.append(string)
        return "".join(stack)
