class Solution:
    from collections import defaultdict
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # index = defaultdict(int)
        # res = []
        # arr_s = sorted(set(arr))


        # for i, n in enumerate(arr_s):
        #     index[n] = i+1
        #     # print(index)

        # for e in arr:
        #     for key, value in index.items():
        #         if key == e:
        #             res.append(value)

        # return res


        index = {}
        # res = []
        arr_s = sorted(set(arr))


        for i in range(len(arr_s)):
            index[arr_s[i]] = i+1
            # print(index)

        for i in range(len(arr)):
            arr[i] = index[arr[i]]

        return arr