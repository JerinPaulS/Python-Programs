'''
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp, slow, fast = head, head, head
        
        while fast is not None and fast.next is not None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            
        temp.next = None
        
        left_subtree = self.sortList(head)
        right_subtree = self.sortList(slow)
        
        return self.merge(left_subtree, right_subtree)
    
    def merge(self, head1, head2):
        dummy = ListNode(-1)
        curr = dummy
        
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            
        if head1 is not None:
            curr.next = head1
        if head2 is not None:
            curr.next = head2
        
        return dummy.next