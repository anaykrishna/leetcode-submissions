# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev 

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = self.reverse(slow.next)
        slow.next = None
        
        while second:
            nxt1 = first.next
            nxt2 = second.next
            
            first.next = second
            second.next = nxt1
            
            first = nxt1
            second = nxt2


