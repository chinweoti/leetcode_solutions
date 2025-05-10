class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) -1

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




        # result = list(s)
        # n = len(s)          
        # for i in range(n // 2):
        #     result[i] = result[n - i - 1] = min(s[i], s[n - i - 1])
        # return ''.join(result)