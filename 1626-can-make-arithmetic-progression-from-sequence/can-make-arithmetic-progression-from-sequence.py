class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # more efficient
        arr.sort()
        diff=arr[1]-arr[0]
        for i in range(2,len(arr)):
         if arr[i]-arr[i-1]!=diff:
          return False
        return True



        
        # arr.sort()
        # i = 0
        # r = 1
        # res = []
        # while r < len(arr):
        #     diff = abs(arr[i] - arr[r])
        #     if abs(arr[i] - arr[r]) == diff:
        #         i += 1
        #         r += 1
        #         res.append(diff)
        #         # print(res)
        # if len(set(res))==1:
        #     return True
        # else:
        #     return False
                