'''
1567. Maximum Length of Subarray With Positive Product
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pos = [0] * n
        neg = [0] * n
        
        if nums[0] > 0:
        	pos[0] = 1
        else:
        	pos[0] = 0
        if nums[0] < 0:
        	neg[0] = 1
        else:
        	neg[0] = 0
        
        for i in range(1, n):
            if nums[i] < 0:
            	if neg[i - 1]:
            		pos[i] = 1 + neg[i - 1]
            	else:
            		pos[i] = 0
                if pos[i - 1]:
                	neg[i] = 1 + pos[i - 1]
                else:
                	neg[i] = 1
            elif nums[i] > 0:
                if pos[i - 1]:
                	pos[i] = 1 + pos[i - 1]
                else:
                	pos[i] = 1
                if neg[i - 1]:
                	neg[i] = 1 + neg[i - 1]
                else:
                	neg[i] = 0
        return max(pos)