class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = k
        i = len(num) - 1

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
            res.append(carry % 10)
            carry //= 10
            i -= 1

        return res[::-1]

        # carry = 0
        # num.reverse()
        # l = 0
        # r = 0
        # k = str(k)
        # k = k[::-1]
        # # print(k)
        # while l < len(str(k)) and r < len(str(k)):
        #     total = (num[l] + int(k[r]) + carry)
        #     # print(total, carry, int(k[r]))
        #     if total > 9:
        #         carry += total // 10
        #         # print(carry)
        #         rem = total % 10
        #         print(rem)
        #         num[l] = rem
        #         l += 1 
        #         r += 1
        #     elif total <= 9:
        #         num[l] += total
        #         # print(num[l], total)
        #         l += 1 
        #         r += 1
        #         # print(num)
        # return num[::-1]