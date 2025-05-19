class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        n = ''.join(str(x) for x in num)
        result = int(n) + (k)
        result = (str(result))
        
        res = []
        for e in result:
            res.append(int(e))
        return res
        
        
        
        
        
        
        
        
        
        # res = []
        # carry = k
        # print(k)
        # i = len(num) - 1

        # while i >= 0 or carry > 0:
        #     if i >= 0:
        #         carry += num[i]
        #     res.append(carry % 10)
        #     carry //= 10
        #     i -= 1

        # return res[::-1]

        

        # carry = 0
        # num.reverse()
        # l = 0
        # r = 0
        # k = str(k)[::-1]
        # while l < len(str(k)) and r < len(str(k)):
        #     num[l] = (num[l] + int(k[r]) + carry)
        #     if num[l] >=10:
        #         carry += num[l]// 10
        #         rem = num[l] % 10
        #         num[l] = rem
        #         l += 1 
        #         r += 1
        #     else:
        #         l += 1 
        #         r += 1
        # return num[::-1]