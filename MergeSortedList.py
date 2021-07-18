'''
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
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode (0)
        curr = res
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1 
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
        return res.next

def print_l(l):
    while l != None:
        print(l.val)
        l = l.next

obj = Solution()
l1 = ListNode(-9)
l1.next = ListNode(3)
#l1.next.next = ListNode(4)
l2 = ListNode(5)
l2.next = ListNode(7)
#l2.next.next = ListNode(4)
print_l(obj.mergeTwoLists(l1, l2))
#print_l(obj.mergeTwoLists([],[]))
#print_l(obj.mergeTwoLists([],[0]))
