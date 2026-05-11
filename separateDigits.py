# class Solution:
#     def separateDigits(self, nums: List[int]) -> List[int]:
#         # result = []
#         # for i in nums:
#         #     a = str(i)
#         #     for j in a :
#         #         result.append(int(j))
#         # return result

        

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            digits = []

            # Handle 0 separately
            if num == 0:
                digits.append(0)

            # Extract digits using modulo and division
            while num > 0:
                digits.append(num % 10)
                num //= 10

            # Reverse because digits come in reverse order
            while digits:
                result.append(digits.pop())

        return result


        
