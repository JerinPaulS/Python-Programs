'''
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""	
		if not lists or len(lists) == 0:
			return None	

		while len(lists) > 1:
			result =[]
			for index in range(0, len(lists), 2):
				list1 = lists[index]
				if index + 1 >= len(lists):
					list2 = None
				else:
					list2 = lists[index + 1]
				result.append(self.mergeList(list1, list2))
			lists = result
		return lists[0]

	def mergeList(self, list1, list2):
		if list1 is None:
			return list2
		if list2 is None:
			return list1
		ptr1 = list1
		ptr2 = list2
		dummy = ListNode(-1)
		curr = dummy
		while ptr1 is not None and ptr2 is not None:
			if ptr1.val < ptr2.val:
				temp = ListNode(ptr1.val)
				curr.next = temp
				curr = temp
				ptr1 = ptr1.next
			else:
				temp = ListNode(ptr2.val)
				curr.next = temp
				curr = temp
				ptr2 = ptr2.next

		if ptr1 is not None:
			curr.next = ptr1
		if ptr2 is not None:
			curr.next = ptr2

		return dummy.next