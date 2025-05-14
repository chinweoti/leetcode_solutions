class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph
        p = ''.join(x.lower() if x.isalnum() else ' ' for x in p)
        p = p.split()
        print(p)

        dict = {}

        for e in p:
            if e not in banned:
                print(e, banned)
                dict[e] = dict.get(e, 0)+ 1
        
        for key, value in dict.items():
            print(dict)
            if value == max(dict.values()):
                return key 
