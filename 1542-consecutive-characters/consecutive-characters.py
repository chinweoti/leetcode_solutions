class Solution:
    def maxPower(self, s: str) -> int:
        counter = 0
        max_counter = 0
        n = list(s)
        l = 0
        r = 1

        while r < len(s):
            if n[l] != n[r]:
                l += 1
                r += 1
                counter = 0
            else:
                counter += 1
                l += 1
                r += 1
            max_counter = max(counter, max_counter) 
        return max_counter + 1



        # curr = s[0]
        # temp = 1
        # res = 1

        # for char in s[1:]:
        #     if char == curr:
        #         temp += 1
        #         res = max(temp, res)
        #     else:
        #         curr = char
        #         temp = 1
        # return res