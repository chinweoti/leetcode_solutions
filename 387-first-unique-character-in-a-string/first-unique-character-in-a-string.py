class Solution:
    def firstUniqChar(self, s: str) -> int:
        # # build hash map: character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1



        # char_count = {}
        
        # # Count the frequency of each character
        # for char in s:
        #     char_count[char] = char_count.get(char, 0) + 1
        #     print(char_count)
        
        # # Find the index of the first unique character
        # for index, char in enumerate(s):
        #     if char_count[char] == 1:
        #         return index
        
        # return -1