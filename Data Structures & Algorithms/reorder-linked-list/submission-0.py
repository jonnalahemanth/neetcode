# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        slow.next = None

        # Revers the list
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        
        # attach both linked lists
        list1, list2 = head, prev
        while list2:
            nxt1 = list1.next
            nxt2 = list2.next

            list1.next = list2
            list2.next = nxt1

            list1 = nxt1
            list2 = nxt2

        



        