class Solution:
    def isBalanced(self, num: str) -> bool:
        even_count = 0
        odd_count = 0
        for idx,val in enumerate(num):
            if idx % 2 == 0:
                even_count += int(val)
            else:
                odd_count += int(val)
        return even_count == odd_count
        
