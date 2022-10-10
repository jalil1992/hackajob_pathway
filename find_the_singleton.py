class Solution:
    def run(self, x):
        ans = 0
        x.sort()
        half = len(x) // 2
        for i in range(0, half + 1):
            if i == half:
                ans = x[-1]
                break
            if x[2 * i] != x[2 * i + 1]:
                ans = x[2 * i]
                break

        return ans
