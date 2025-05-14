class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_counter = 0
        # other = ['+','-', '*', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for e in s:
            if e == '(':
                counter += 1
                max_counter = max(max_counter, counter)
            elif e == ')':
                counter -= 1
        return max_counter