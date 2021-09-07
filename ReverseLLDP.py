'''
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		#Iterative
		'''
		if head is None:
		return head
		prev = None
		curr = head
		while curr is not None:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
		return prev
		'''
		#Recursive
		if head is None or head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next, head.next = head, None
            return new_head

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

obj = Solution()
print(obj.reverseList(root))        