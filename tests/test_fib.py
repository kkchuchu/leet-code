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

    def test_climb_case1(self):
        self.assertEquals(2, Sol().climbStairs(2))

    def test_climb_case2(self):
        self.assertEquals(3, Sol().climbStairs(3))

    def test_minCostClimbingStairs_case1(self):
        self.assertEquals(15, Sol().minCostClimbingStairs([10, 15, 20]))

    def test_minCostClimbingStairs_case2(self):
        self.assertEquals(6, Sol().minCostClimbingStairs(
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

    def test_rob_case1(self):
        self.assertEquals(4, Sol().rob([1, 2, 3, 1]))
        
    def test_rob_case2(self):
        self.assertEquals(12, Sol().rob([2,7,9,3,1]))
