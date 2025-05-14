class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        return address.replace(".","[.]")


        # res = ""
        
        # for e in address:
        #     if e != ".":
        #         res += e
        #     else:
        #         res += '[.]'

        # return res