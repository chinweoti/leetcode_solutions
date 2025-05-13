class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = "0"

        for i in range(len(number)):
            if number[i] == digit:
                check = number[:i] + number[i+1:]
                if check > max_num:
                    max_num = check
        return max_num

