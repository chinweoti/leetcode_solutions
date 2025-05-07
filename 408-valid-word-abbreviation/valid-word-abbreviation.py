class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pointer = 0 
        abbr_pointer = 0

        while pointer < len(word) and abbr_pointer < len(abbr):
            if abbr[abbr_pointer].isdigit():
                steps = 0

                if abbr[abbr_pointer] == "0":
                    return False
                
                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    steps = steps * 10 + int(abbr[abbr_pointer])

                    abbr_pointer += 1

                pointer += steps
            else: 
                if word[pointer] != abbr[abbr_pointer]:
                    return False
                
                pointer += 1
                abbr_pointer += 1
        return pointer == len(word) and abbr_pointer == len (abbr)