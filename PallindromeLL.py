'''
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast_ptr = head
        slow_ptr = head

        while fast_ptr is not None and fast_ptr.next is None:
        	fast_ptr =fast_ptr.next.next
        	slow_ptr = slow_ptr.next

        prev_ptr = None
        while slow_ptr is not None:
        	temp = slow.next
        	slow_ptr.next = prev_ptr
        	prev_ptr = slow_ptr
        	slow_ptr = temp

        start_ptr = head
        end_ptr = prev_ptr
        while end_ptr is not None:
        	if start_ptr.val != end_ptr.val:
        		return False
        	end_ptr = end_ptr.next
        	start_ptr = start_ptr.next

        return True