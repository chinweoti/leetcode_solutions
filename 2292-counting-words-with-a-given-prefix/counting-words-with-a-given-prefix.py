class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        f = len(pref)

        for e in words:
            if e[:f] == pref:
                counter += 1
        return counter