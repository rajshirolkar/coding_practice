# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Own working solution
        # if head.next == None:
        #     return None
        # l = 0
        # cur = head
        # while cur:
        #     l += 1
        #     cur = cur.next
        # print(l)
        # res = l - n
        # if res == 0:
        #     return head.next
        # cur = head
        # for i in range(0,res-1):
        #     cur = cur.next
        
        # cur.next = cur.next.next
        # return head
        
        # Neet Code
        r = head
        dum = ListNode(0, head)
        l = dum
        while n>0 and r:
            r=r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dum.next