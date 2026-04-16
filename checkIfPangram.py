class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dicv  = {}
        for i in sentence:
            
            dicv[i] = 1
            
        if len(dicv) == 26:
            return True
        else:
            return False

        # a =  sorted(sentence)
        # return len(set(a)) == 26

        # se = set()
        # for i in sentence:
        #     se.add(i)
        # return len(se) == 26
