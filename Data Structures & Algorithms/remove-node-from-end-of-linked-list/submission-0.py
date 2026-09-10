# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, head
        for i in range(n):
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next
        

        