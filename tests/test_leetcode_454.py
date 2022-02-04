import unittest

from leetcode.leetcode_454 import Solution as Sol


class Test454(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_case1(self):
        r = Sol().fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])
        self.assertEquals(1, r)
        
    def test_case2(self):
        r = Sol().fourSumCount([1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
        self.assertEquals(2, r)
        
    def test_case3(self):
        r = Sol().fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1])
        self.assertEquals(6, r)