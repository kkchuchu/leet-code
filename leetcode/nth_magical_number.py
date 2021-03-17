class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int):
        pass
    
    def gcd(self, x, y):
        while y:
            x, y = y, x%y
        return x
    
    def lcm(self, x, y):
        return x * y // lcm(x, y)
