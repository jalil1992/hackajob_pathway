class Solution:
    def run(self, n, m, movies):
        x = [i for i in range(1, n + 1)]
        ans = []
        for y in movies:
            ans.append(x.index(y))
            x.remove(y)
            x.insert(0, y)
            print(x, ans)
        return ",".join([str(v) for v in ans])


sol = Solution()
print(sol.run(3, 3, [3, 1, 1]))
