class Solution:
    def reverseWords(self, s: str) -> str:
        str_s = s.split()
        str_s.reverse()
        return ' '.join(str_s)