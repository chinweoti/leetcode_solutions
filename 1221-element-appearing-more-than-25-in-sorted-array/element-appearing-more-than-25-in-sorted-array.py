class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        count_map = defaultdict(int)
        n = len(arr)//4

        for e in arr:
            count_map[e] += 1

        for key, value in count_map.items():
            if value > n:
                return key
        return - 1
        