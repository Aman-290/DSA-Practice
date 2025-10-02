# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        l3 = dummy
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next

        # attach the rest of whichever list is not empty
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2

        return dummy.next