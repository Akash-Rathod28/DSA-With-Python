class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")

        string = ""
        for i in a:
            string+=i[::-1]
            string += " "
        return string[:len(string)-1]
            
