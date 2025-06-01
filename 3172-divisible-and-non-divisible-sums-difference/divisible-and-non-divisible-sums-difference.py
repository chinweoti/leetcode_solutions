class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_div = 0
        div = 0

        for e in range(1, n+1):
            if e % m == 0:
                div += e
                # print(div)
            elif e % m != 0:
                not_div += e
                # print(not_div)
        return (not_div - div)