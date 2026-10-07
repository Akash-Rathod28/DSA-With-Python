class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # Start BFS with the original string
        current_level = {s}
        
        while True:
            # Find all valid strings in the current level
            valid_results = [st for st in current_level if isValid(st)]
            
            # If we found any valid strings, we've achieved the minimum removals
            if valid_results:
                return valid_results
            
            # Otherwise, generate the next level by removing one parenthesis at each position
            next_level = set()
            for st in current_level:
                for i in range(len(st)):
                    if st[i] in ('(', ')'):
                        next_level.add(st[:i] + st[i+1:])
            
            current_level = next_level
