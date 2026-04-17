class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        val = "" # "dfedcba"
        for i in word:
            if i == ch:
                val += i
                break
            else:
                val += i
        val =  val[::-1]  
        a = word.find(ch)
        return val + word[a+1:]
