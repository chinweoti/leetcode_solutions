class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        heights_map = dict(zip(heights, names))

        res = []
        heights.sort(reverse=True)
        for e in heights:
            res.append(heights_map[e])
        return res

