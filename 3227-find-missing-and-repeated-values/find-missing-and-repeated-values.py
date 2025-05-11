class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        hashmap = {}

        if len(grid) == 0:
            return 0

        for row in grid:
            for e in row:
                if e not in hashmap:
                    hashmap[e] = hashmap.get(e, 0)+ 1
                else:
                    repeat_num = e
        
        for d in range(1, (len(grid[0])*len(grid))+1):
            if d not in hashmap:
                missing = d
        return [repeat_num, missing]
