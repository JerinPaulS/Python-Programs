'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        start = head
        if current is None:
            return(head)
        else:
            current = current.next
            while current:
                if current.val == start.val:
                    current = current.next
                else:
                    start.next = current
                    start = start.next

        start.next = None
        return(head)

def print_l(head):
	while head:
		print(head.val)
		head = head.next

obj = Solution()
head = ListNode(1)
#head.next = ListNode(1)
#head.next.next = ListNode(2)
#head.next.next.next = ListNode(3)
#head.next.next.next.next = ListNode(3)
print_l(obj.deleteDuplicates(head))