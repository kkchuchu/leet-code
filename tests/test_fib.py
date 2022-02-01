import unittest
from leetcode.leetcode_509 import Solution as Sol

class TestFibDP(unittest.TestCase):

    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_case1(self):
        self.assertEquals(1, Sol().fib(1))
    
    def test_case0(self):
        self.assertEquals(0, Sol().fib(0))
        
    def test_case2(self):
        self.assertEquals(1, Sol().fib(2))
        
    def test_tribonacci_case1(self):
        self.assertEquals(2, Sol().tribonacci(3))
        
    def test_tribonacci_case2(self):
        self.assertEquals(4, Sol().tribonacci(4))
        
    def test_tribonacci_case3(self):
        self.assertEquals(1389537, Sol().tribonacci(25))