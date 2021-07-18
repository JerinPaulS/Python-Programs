'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
        	return head
        temp = self.removeElements(head.next, val)
        if head.val == val:
        	return temp
    	head.next = temp
    	return head
        

def print_ele(root):
	while root:
		print root.val
		root = root.next

root = ListNode(6)
root.next = ListNode(2)
root.next.next = ListNode(6)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(4)
root.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next = ListNode(6)

obj = Solution()
print_ele(obj.removeElements(root, 6))


'''
if head is None:
        	return None
        mainptr = head
        while head.val == val and head is not None:
        	head = head.next
        	mainptr.next = None
        	mainptr = head
        if head is None or head.next is None:
        	return head
        else:
        	currptr = head.next
        while currptr is not None:
        	if currptr.val == val:
        		mainptr.next = currptr.next
        		currptr.next = None
        		currptr = mainptr.next
        	else:
        		mainptr = mainptr.next
        		currptr = currptr.next
        return head
'''