class Solution:
    def run(self, a):
        max_len = [1] * len(a)
        for i in range(1, len(a)):
            for j in range(0, i):
                if a[i] > a[j]:
                    max_len[i] = max(max_len[i], max_len[j] + 1)

        ans = max(max_len)
        return ans


sol = Solution()
print(sol.run([6, 2, 0, -2, 3, 8, 1, 6, 23, 19, 65]))
