class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])

        if reversed2 == num:
            return True
        return False