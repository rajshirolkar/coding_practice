# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp, fp = head, head

        while fp is not None and fp.next is not None:
            sp = sp.next
            fp = fp.next.next
        return sp