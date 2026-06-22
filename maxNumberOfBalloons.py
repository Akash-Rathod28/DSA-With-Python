class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count = 0
        # string = ""
        # for val in text:
        #     if val in "ballon":
        #         string += val
        # if len(string) != len("ballon"):
        #     return 0
        # while True:
        #     n = 6
        #     if string[]

        
        
        counts = Counter(text)
        
       
        b = counts['b']
        a = counts['a']
        l = counts['l'] // 2
        o = counts['o'] // 2
        n = counts['n']
        
        
        return min(b, a, l, o, n)
            
            
        
