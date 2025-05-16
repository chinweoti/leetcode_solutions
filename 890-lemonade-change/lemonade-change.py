class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b5, b10 = 0, 0

        for e in bills:
            if e == 5:
                b5 += 1
            if e == 10:
                b10 += 1
                if b5:
                    b5 -= 1
                else:
                    return False
            if e == 20:
                if b10 and b5:
                    b10 -= 1
                    b5 -= 1
                elif b5 >= 3:
                    b5 -= 3
                else:
                    return False
                    print(e, b5, b10)
        return True

