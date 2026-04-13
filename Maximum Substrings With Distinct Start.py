class Solution:
    def maxDistinct(self, s: str) -> int:
        # se = set()
        # for seen in s:
        #     if seen not in se:
        #         se.add(seen)
        # return len(se)

        #  # another method
        # dic = {}
        # for i in s:
        #     if i not in dic:
        #         dic.update({i:1})
        # count = 0
        # for key,values in dic.items():
        #     count += values
        # return count

        # return len(set(s))

        # another method
        dig = {}
        for i in s:
            dig[i] = 1
        return len(dig)


      
        
