class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')

        res = [e[::-1] for e in s]
        return ' '. join(res)