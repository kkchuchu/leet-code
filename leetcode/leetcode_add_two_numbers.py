# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_value_from_listnode(l: ListNode):
    c = l
    i_10 = 1
    r = 0
    while c is not None:
        r = r + i_10 * c.val
        
        c = c.next
        i_10 = i_10 * 10
    return r

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_c, l2_c = l1, l2
        add_one = 0
        ans = ListNode()
        ans_c = ans
        while True:
            if l1_c is None:
                l1_c_value = 0
            else:
                l1_c_value = l1_c.val
                l1_c = l1_c.next
            
            if l2_c is None:
                l2_c_value = 0
            else:
                l2_c_value = l2_c.val
                l2_c = l2_c.next
                
            this_value = l1_c_value + add_one + l2_c_value
            add_one = this_value // 10
            this_value = this_value % 10
            
            ans_c.val = this_value
            
            
            if l1_c is None and l2_c is None:
                if add_one == 0:
                    ans_c.next = None
                else:
                    ans_c.next = ListNode(
                        val=1,
                        next=None
                    )
                break
            
            ans_c.next = ListNode()
            ans_c = ans_c.next
            
        return ans
            