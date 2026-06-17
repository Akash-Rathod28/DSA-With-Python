# class Solution:
#     def processStr(self, s: str, k: int) -> str:
#         result = ""

#         for i in s:
#             if i.islower():
#                 result += i
#             elif i == "*":
#                 if len(result) >= 1:
#                     result = result[:len(result)-1]
#             elif i == "#":
#                 result = result + result
#             else:
#                 result = result[::-1]
#         try:
#             return result[k]
#         except:
#             return "."

class Solution:
    def processStr(self, s: str, k: int) -> str:
        operations = []
        current_len = 0

        for char in s:
            if char.islower():
                current_len += 1
                operations.append((1, char))
            elif char == "*":
                if current_len > 0:
                    current_len -= 1
                    operations.append((2, None))
            elif char == "#":
                current_len *= 2
                operations.append((3, None))
            else:
                operations.append((4, None))

        if k < 0 or k >= current_len:
            return "."

        for op_type, char in reversed(operations):
            if op_type == 1:
                if k == current_len - 1:
                    return char
                current_len -= 1
            elif op_type == 2:
                current_len += 1
            elif op_type == 3:
                current_len //= 2
                k %= current_len
            elif op_type == 4:
                k = current_len - 1 - k

        return "."
