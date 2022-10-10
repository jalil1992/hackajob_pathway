class Solution:
    def run(self, x, y):
        if x > y:
            x, y = y, x

        # make both in the same level
        bx = "{0:b}".format(x)
        by = "{0:b}".format(y)
        by = by[: len(bx)]
        y = int(by, 2)

        while x != y:
            x //= 2
            y //= 2

        return x


sol = Solution()
print(sol.run(13, 15))
print(sol.run(11, 13))
print(sol.run(10, 11))
print(sol.run(25, 100))
print(sol.run(25, 101))
