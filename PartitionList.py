'''
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        curr = head
        left = dummy1
        right = dummy2
        while curr is not None:
            if curr.val < x:
                if left == dummy1:
                    dummy1.next = curr
                else:
                    left.next = curr
                left = left.next
            else:
                if right == dummy2:
                    dummy2.next = curr
                else:
                    right.next = curr
                right = right.next
            temp = curr.next
            curr.next = None
            curr = temp
            
        left.next = dummy2.next
        return dummy1.next