'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        start = 0
        end = len(arr) - k
        while start < end:
        	mid = (start + end - 1) / 2
        	if(x - arr[mid]) > (arr[mid + k] - x):
        		start = mid + 1
        	else:
        		end = mid
        return(arr[start:start + k])

obj = Solution()
print(obj.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
print(obj.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))