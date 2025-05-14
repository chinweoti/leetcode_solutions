class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        count_map = defaultdict(int)

        for e in arr:
            count_map[e] += 1

        for key, value in count_map.items():
            if value > len(arr)//4:
                return key
        