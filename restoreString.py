class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # li = [""]*len(s)
        # for i,char in enumerate(s):
        #     li[indices[i]] = char
        # return "".join(li)

        mapping = dict(zip(indices, s))
        
        # Build the string by looking up 0, 1, 2...
        result = ""
        for i in range(len(s)):
            result += mapping[i]
            
        return result
        

        
