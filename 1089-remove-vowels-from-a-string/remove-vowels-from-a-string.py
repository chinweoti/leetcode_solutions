class Solution:
    def removeVowels(self, s: str) -> str:
        
        vowels = 'AEIOUaeiou'
        
        s = list(s)
        res = ''

        for e in s:
            if e not in vowels:
                res += e
        return res
