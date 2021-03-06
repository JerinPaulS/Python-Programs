'''
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]
Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]
 

Constraints:

3 <= arr.length <= 3 * 104
arr[i] is 0 or 1

[1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1]

'''
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        count_ones = arr.count(1)
        if count_ones == 0:
        	return [0, 2]
        if count_ones % 3 != 0:
        	return [-1, -1]
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        count = 0
        div_count = count_ones // 3
        for index in range(len(arr)):
        	if arr[index] == 1:
        		if count == 0:
        		 	ptr1 = index
        		elif count == div_count:
        			ptr2 = index
        		elif count == div_count * 2:
        			ptr3 = index
        			break
        		count = count + 1
        org_ptr2 = ptr2
        org_ptr3 = ptr3
        while ptr3 < len(arr) and ptr1 < org_ptr2 and ptr2 < org_ptr3:
        	if arr[ptr1] != arr[ptr2] or arr[ptr2] != arr[ptr3]:
        		return [-1, -1]
        	else:
        		ptr1 = ptr1 + 1
        		ptr2 = ptr2 + 1
        		ptr3 = ptr3 + 1
        if ptr3 == len(arr):
        	return [ptr1 - 1, ptr2]
        else:
        	return [-1, -1]