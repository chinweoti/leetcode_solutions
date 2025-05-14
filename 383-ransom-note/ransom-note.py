class Solution:
    from collections import defaultdict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # mMap = Counter(magazine)
        # # print(mMap)
        # rMap = Counter(ransomNote)
        # # print(rMap)

        # for char in rMap:
        #     if char not in mMap:
        #         return False
        #     if rMap[char] > mMap[char]:
        #         return False
        
        # return True


        # ransomNote_set = set(ransomNote)
        for l in ransomNote:
            if ransomNote.count(l) > magazine.count(l):
                return False
        return True


        # note = defaultdict(int)

        # if len(magazine) < len(ransomNote):
        #     return False


        # for i in range(len(magazine)):
        #     note[magazine[i]] += 1
        #     print(note)
            
        # for e in ransomNote:    
        #     if e not in note: 
        #         print(e)
        #         return False
        #     else:
        #         if note[e]> 0:
        #             note[e] -= 1
        #             print(e)

        # return True

        

