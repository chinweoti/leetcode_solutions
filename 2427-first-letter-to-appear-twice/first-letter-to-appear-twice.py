class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hashmap= defaultdict(int)

        for e in s:
            if e in hashmap:
                return e
            hashmap[e] += 1