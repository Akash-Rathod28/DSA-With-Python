class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        
        # s = ""
        # con = ""

        # for i in range(4):
        #     con += date[i]
        # a = int(con)
        # s += format(a, 'b')
        # s += "-"

        # con = ""
        # for i in range(5, 7):
        #     con += date[i]
        # a = int(con)
        # s += format(a, 'b')
        # s += "-"

        # con = ""
        # for i in range(8, len(date)):
        #     con += date[i]
        # a = int(con)
        # s += format(a, 'b')

        # return s

        # return "-".join(format(int(part), "b") for part in date.split("-"))


        date = date.split("-")
        res = ""
        for i,part in enumerate(date):
            res += format(int(part),"b")
            if i != len(part):
                res += "-"
            
        return res
        
