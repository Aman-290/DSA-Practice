# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        current3=l3
        current1=l1
        current2=l2
        carry=0
        while current1 or current2 or carry:
            val1=current1.val if current1 else 0
            val2=current2.val if current2 else 0

            total = val1+val2+carry    
            current3.next = ListNode(total%10)
            carry = total//10
            current3=current3.next
            
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
        
        return l3.next

                
        
        