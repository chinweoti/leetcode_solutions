class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        sentence = sentence.split()
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        add = 1
        res = []

        for i, n in enumerate(sentence):
            if n[0] in vowel:
                n +=  "ma"  + (add * 'a')
                add += 1
                res.append(n)
            else:
                n = n[1:len(n)] + n[0] + 'ma' + (add * 'a')
                add += 1
                res.append(n)
        return ' '.join(res)
