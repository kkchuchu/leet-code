import unittest

from leetcode.leetcode_add_two_numbers import ListNode
from leetcode.leetcode_add_two_numbers import Solution as Sol
from leetcode.leetcode_add_two_numbers import get_value_from_listnode


class TestAddTwoNumbers(unittest.TestCase):

    def setUp(self):
        self._l1 = ListNode(
            val=2,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=3,
                    next=None
                )
            )
        )
        self._l2 = ListNode(
            val=5,
            next=ListNode(
                val=6,
                next=ListNode(
                    val=4,
                    next=None
                )
            )
        )
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_case1(self):
        r = Sol().addTwoNumbers(self._l1, self._l2)
        self.assertEquals(807, get_value_from_listnode(r))
