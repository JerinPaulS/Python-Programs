'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        head = ListNode(-1)
        temp = head
        while ptr1 is not None and ptr2 is not None:
        	if ptr1.val < ptr2.val:
        		curr = ListNode(ptr1.val)
        		temp.next = curr
        		ptr1 = ptr1.next
        	else:
        		curr = ListNode(ptr2.val)
        		temp.next = curr
        		ptr2 = ptr2.next
        	temp = temp.next
        if ptr1 is not None:
        	temp.next = ptr1
        if ptr2 is not None:
        	temp.next = ptr2
        return head.next