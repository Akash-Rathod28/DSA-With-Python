class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # num = []
        # for i in order:
        #     if i in friends:
        #         num.append(i)
        # return num
        
        friends_set = set(friends)
        num = []
        for i in order:
            if i in friends_set:
                num.append(i)
        return num
