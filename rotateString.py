class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # a = s.find(goal[0])
        # # if a == len(s)-1:
        # #     return s[-1]+s[:a] == goal
        # b = s.find(goal[-1])
        # return s[a:]+s[:a] == goal
        for i in range(len(s)):
            rotate = s[-i:] + s[:-i]
            if rotate == goal:
                return True
        return False

       
