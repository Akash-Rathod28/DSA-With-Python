class Solution:
    def reverseDegree(self, s: str) -> int:
        # a = []
        # j = 1
        # for i in range(len(s)):
        #     a.append(ord(s[i]) * 1 )
        #     j += 1
        # return sum(a)

        # alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        # val = (26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1)
        # j = 1
        # # li = []
        # count = 0

        # for i in s:
        #     a = alpha.index(i)
        #     # li.append(val[a]*j)
        #     count += val[a] * j
        #     j += 1
        # return count


        # div = {
        #     'a' : 26,
        #     'b' : 25,
        #     'c' : 24,
        #     'd' : 23,
        #     'e' : 22,
        #     'f' : 21,
        #     'g' : 20,
        #     'h' : 19,
        #     'i' : 18,
        #     'j' : 17,
        #     'k' : 16,
        #     'l' : 15,
        #     'm' : 14,
        #     'n' : 13,
        #     'o' : 12,
        #     'p' : 11,
        #     'q' : 10,
        #     'r' : 9,
        #     's' : 8,
        #     't' : 7,
        #     'u' : 6,
        #     'v' : 5,
        #     'w' : 4,
        #     'x' : 3,
        #     'y' : 2,
        #     'z' : 1,
        # }  
        # count = 0  
        # j   = 1
        # for i in s:
        #     count += div[i]*j
        #     j +=1
        # return count


        count = 0
        
        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            count += value * (i + 1)
        
        return count

