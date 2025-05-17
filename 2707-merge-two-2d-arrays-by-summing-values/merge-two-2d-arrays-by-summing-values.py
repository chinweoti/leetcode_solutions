class Solution:
    from collections import defaultdict
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        

        res = defaultdict(int)
        result = []

        for id, value in nums1:
            res[id] += value
            # print(res)
        
        for id, value in nums2:
            res[id] += value
            # print(res)

        for k, v in res.items():
            result.append([k,v])
            # print(result)
            result.sort()
        return result




















        # result = defaultdict(int)
        # res= []
        # for id, value in nums1:
        #     result[id] += value
        #     print(result)
        # for id, value in nums2:
        #     result[id] +=  value
        #     print(result)

        # for key, value in result.items():
        #     res.append([key, value])
        #     print(res)
        #     res.sort()
        #     print(res)
        # return res
        # # return [[id, value] for id, value in sorted(result.items())]