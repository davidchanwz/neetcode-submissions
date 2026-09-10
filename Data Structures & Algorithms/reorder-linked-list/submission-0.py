# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        slow.next = None
        cur, prev = list2, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        list2 = prev
        dummy = ListNode()
        cur = dummy
        while head and list2:
            cur.next = head
            tmp = head.next
            head = list2
            list2 = tmp
            cur = cur.next
        if head:
            cur.next = head
        if list2:
            cur.next = list2
        