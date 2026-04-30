class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        word = []
        for i in words:
            a = i.split(separator)
            for j in a:
                if j != "":
                    word.append(j)
        return word
