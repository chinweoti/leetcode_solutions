class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
     
        for i in range(len(s) - 1):
            x = (ord(s[i]) - ord('a'))
            y = (ord(s[i+1]) - ord('a'))
            score += abs(x- y)
        return score


        # score = 0
        # for i in range(len(s) - 1):
        #     score += abs(ord(s[i]) - ord(s[i + 1]))
        # return score