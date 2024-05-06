# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            while stack and stack[-1] < node.val:
                stack.pop()
            stack.append(node.val)
            node = node.next
        
        dummy = ListNode()
        curr = dummy
        for n in stack:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next
        

            
