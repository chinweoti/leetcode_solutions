class Solution:
    def removeVowels(self, s: str) -> str:
        
        vowels = 'AEIOUaeiou'
        
        res = ''

        for e in s:
            if e not in vowels:
                res += e
        return res
