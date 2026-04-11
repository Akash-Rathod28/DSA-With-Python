class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        i = 0
        while i < len(words):
            if x in words[i]:
                result.append(i)
            i += 1
                
        return result
        # for idx,word in enumerate(words):
        #     if x in word:
        #         result.append(idx)
        # return result

        
