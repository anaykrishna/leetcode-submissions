# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        head = list1

        while list1 and list2:
            prev = None

            while list1 and list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            
            prev.next = list2
            list1, list2 = list2, list1
        
        return head

            
        
