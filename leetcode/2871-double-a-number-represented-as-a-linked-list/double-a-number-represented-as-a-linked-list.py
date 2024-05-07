# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize an empty list to store the values of the linked list
        values = []
        val = 0

        # Traverse the linked list and push its values onto the list
        while head is not None:
            values.append(head.val)
            head = head.next

        new_tail = None

        # Iterate over the list of values and the carryover
        while values or val != 0:
            # Create a new ListNode with value 0 and the previous tail as its next node
            new_tail = ListNode(0, new_tail)

            # Calculate the new value for the current node
            # by doubling the last digit, adding carry, and getting the remainder
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10

        # Return the tail of the new linked list
        return new_tail

        # res = 0
        # lst = []
        # node = head
        # mul = 0
        # while node:
        #     # res += str(node.val)
        #     lst.append(node.val)
        #     node = node.next
        # for i, n in enumerate(lst[::-1]):
        #     res += (10 * i + n) 
        # # ans = int(res) * 2
        # # ans = str(ans)
        # res *= 2
        # dummy = ListNode()
        # curr = dummy
        # res = str(res)
        # for c in res:
        #     newnode = ListNode(int(c))
        #     curr.next = newnode
        #     curr = curr.next
        # return dummy.next