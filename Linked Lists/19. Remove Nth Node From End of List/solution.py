from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer approach: moving one pointer to be 
        # n steps ahead from the other

        # t/c: O(l) l = length of the list, s/c: O(1)

        result = ListNode()
        result.next = head

        back = result
        front = result

        for i in range(n + 1):
            front = front.next

        while front != None:
            front = front.next
            back = back.next

        back.next = back.next.next

        return result.next


