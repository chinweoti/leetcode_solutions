class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = defaultdict(int)

        for value, weight in items1:
            res[value] += weight
        
        for value, weight in items2:
            res[value] += weight
        
        result = [[k, v] for k, v in sorted(res.items())]
        return result