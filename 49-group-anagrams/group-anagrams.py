class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            # print(key)
            anagram_map[key].append(word)
        return list(anagram_map.values())




        res = defaultdict(list) #to map char count to list of Anagrams

        for s in strs:
            count = [0] * 26 #count of each word from a - z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
            # print(res)
        return list(res.values())





        # res = defaultdict(list)
        # # print(res)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     print(sortedS, s)
        #     res[sortedS].append(s)
        #     print(res)
        # return list(res.values())

        # # time complexity = O(m.nlogn)
