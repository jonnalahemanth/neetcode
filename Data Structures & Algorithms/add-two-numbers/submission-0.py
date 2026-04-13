# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2

        dummy = ListNode()
        tail = dummy
        carry = 0

        while c1 or c2 or carry:
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0
            digit, carry = (val1+val2+carry)%10, (val1+val2+carry)//10
            tail.next = ListNode(digit)
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
            tail = tail.next
        
        return dummy.next



        