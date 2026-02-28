class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.replace(".","[.]")
        return a
        
        # a = ""
        # for i in address:
        #     if i == ".":
        #         a += "[.]"
        #     else:
        #         a += i
                
        # return a
                
    
