
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int):
        a, b, c = min(a, b), max(a, b), self.lcm(a, b)
        a_less_c = [ a*i for i in range(1, c//a) if a*i < c]
        b_less_c = [ b*i for i in range(1, c//b) if b*i < c]
        residue2n = [0] + sorted(list(set(a_less_c + b_less_c)))
        r = (n // len(residue2n))*c + residue2n[n%len(residue2n)]
        
        # from pdb import set_trace; set_trace()
        return r % (10**9 + 7)

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x * y // self.gcd(x, y)


print(Solution().nthMagicalNumber(4, 2, 3))  # 6
print(Solution().nthMagicalNumber(5, 2, 4))  # 10
print(Solution().nthMagicalNumber(1, 2, 3))  # 2
print(Solution().nthMagicalNumber(2, 2, 3))  # 3
print(Solution().nthMagicalNumber(1000000000, 40000, 40000))
print(Solution().nthMagicalNumber(1000000000, 39999, 40000))
"""
2, 4, 4
4, 8, 8
6, 12, 12
8,
"""
