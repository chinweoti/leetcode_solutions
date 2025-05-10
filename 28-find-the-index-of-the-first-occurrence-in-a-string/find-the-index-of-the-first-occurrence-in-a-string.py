class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == "":
        #     return 0
        # # since we are lloking for the first occurence of the needle it is impossible that it exists at a length greater than the lenght of the needle hence: len(haystack)+ 1 - len(needle)
        # for i in range(len(haystack)+ 1 - len(needle)):
        #     # use a nested for loop to check for needle within haystack such that for every index (i) of haystack, it checks the index (j) of needle 
        #     for j in range(len(needle)):
        #         #here j acts as an icreamenter, so if they're not equal then its not a substring, so break
        #         if haystack[i+j] != needle[j]:
        #             break
        #         # when j gets to the length if the needle i.e len(needle) -1 and if we have found a substring, then return the first occurent which we have tracked as i, we return i else we increament i and go through the for loop again
        #         if j == len(needle) - 1:
        #             return i
        # # if after we have go through the for loop, we dont have a match/substring, then we return -1
        # return -1


# another way to solve 
        if needle == "":
            return 0
        for i in range(len(haystack)+ 1 - len(needle)):
            if haystack[i :i + len(needle)] == needle:
                return i
        return -1