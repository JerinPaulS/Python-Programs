'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 
1 1 1 2 3 4 5 6 7 8

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for index in range(len(nums) - 1, 1, -1):
        	left = 0
        	right = index - 1
        	while left < right:
        		if nums[left] + nums[right] > nums[index]:
        			result = result + right - left
        			right = right - 1
        		else:
        			left = left + 1

        return result