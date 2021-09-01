'''
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2

        if len(nums1) > len(nums2):
        	A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        start = 0
        end = len(A) - 1

        while True:
        	i = (start + end) // 2
        	j = half - i - 2

        	leftA = A[i] if i >= 0 else float('-inf')
        	rightA = A[i + 1] if i + 1 < len(A) else float('inf')
        	leftB = B[j] if j >= 0 else float('-inf')
        	rightB = B[j + 1] if j + 1 < len(B) else float('inf')

        	if leftA <= rightB and leftB <= rightA:
        		if total % 2 == 0:
        			return float((max(leftA, leftB) + min(rightB, rightA)) / 2)
        		return min(rightA, rightB)

        	if leftA > rightB:
        		end = i - 1
        	else:
        		start = i + 1