class Solution:
    def run(self, n):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

        ans = ""
        i = 12
        while n:
            div = n // num[i]
            n %= num[i]
            while div:
                ans += sym[i]
                div -= 1
            i -= 1

        n_in_roman_alphabet = ans
        return n_in_roman_alphabet


sol = Solution()
print(sol.run(20395))
