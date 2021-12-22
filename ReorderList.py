'''
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
        	return
        nodes = []
        curr = head
        while curr is not None:
        	nodes.append(curr)
        	curr = curr.next
        curr = head
        flag = 0
        while len(nodes) > 0:
        	if flag:
        		flag = 0
        		node = nodes.pop()
        		node.next = None
        		curr.next = node
        	else:
        		flag = 1
        		node = nodes.pop(0)
        		node.next = None
        		curr.next = node
        	curr = curr.next
        return