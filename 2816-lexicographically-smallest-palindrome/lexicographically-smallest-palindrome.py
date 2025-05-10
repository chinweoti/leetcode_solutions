class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) -1
        counter = 0
        res = list(s)

        while l < r:
            if res[l] == res[r]:
                l += 1
                r -= 1
            elif res[l] != res[r]:
                if res[l] > res[r]:
                    res[l] = res[r]
                else:
                    res[r] = res[l]
        return ''. join(res)




        #  letters = list(s)

        # for i in range(len(s) // 2):
        #     letters[i] = letters[~i] = min(letters[i], letters[~i])

        # return ''.join(letters)