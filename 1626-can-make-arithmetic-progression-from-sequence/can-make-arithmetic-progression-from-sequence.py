class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        i = 0
        r = 1
        res = []
        while r < len(arr):
            diff = abs(arr[i] - arr[r])
            if abs(arr[i] - arr[r]) == diff:
                i += 1
                r += 1
                res.append(diff)
                # print(res)
        if len(set(res))==1:
            return True
        else:
            return False
                