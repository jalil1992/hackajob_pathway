class Solution:
    def run(self, p):
        ans = []
        vowels = ["a", "e", "i", "o", "u"]
        v_idx = []
        c_idx = []
        for i in range(len(p)):
            c = str(p[i]).lower()
            if c in vowels:
                v_idx.append(i)
            elif c.isalpha():
                c_idx.append(i)
        ans.append(f"{len(v_idx)} {len(c_idx)}")

        words = p.split()
        words.reverse()
        ans.append(" ".join([x.swapcase() for x in words]))

        ans.append("-".join(p.split()))

        v_idx.reverse()
        for i in v_idx:
            p = p[:i] + "pv" + p[i:]
        ans.append(p)

        combined_queries = "::".join(ans)
        return combined_queries
