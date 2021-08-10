'''
941. Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        start = 0
        end = len(arr) - 1
        size = len(arr) - 1
        if len(arr) < 3:
        	return False
        for index in range(size):
        	if arr[index] < arr[index + 1]:
        		pass
        	else:
        		start = index
        		break
        for index in range(size, 0, -1):
        	if arr[index - 1] > arr[index]:
        		pass
        	else:
        		end = index
        		break
        return start == end

obj = Solution()
print(obj.validMountainArray([1,2,1]))        