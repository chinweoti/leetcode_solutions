class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list) #to map char count to list of Anagrams

        for s in strings:
            x = []

            for i in range(len(s)-1):
                diff = 26 + ord(s[i+1]) - ord(s[i])
                # print(ord(s[i+1]), ord(s[i]))
                x.append(diff % 26)
                # print(x)
            
            res[tuple(x)].append(s)
            # print(res)
        return list(res.values())