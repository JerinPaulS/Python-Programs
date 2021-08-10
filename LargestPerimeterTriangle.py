'''
976. Largest Perimeter Triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0
Example 3:

Input: nums = [3,2,3,4]
Output: 10
Example 4:

Input: nums = [3,6,2,3]
Output: 8
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
'''
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        for index in range(size - 1, 1, -1):
        	if nums[index] < nums[index - 1] + nums[index - 2]:
        		return nums[index] + nums[index - 1] + nums[index - 2]

        return 0