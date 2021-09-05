'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()

        for index, val in enumerate(nums):
        	if index > 0 and val == nums[index - 1]:
        		continue

        	left = index + 1
        	right = len(nums) - 1

        	while left < right:
        		total = val + nums[left] + nums[right]
        		if total > 0:
        			right = right - 1
        		elif total < 0:
        			left = left + 1
        		else:
        			result.append([val, nums[left], nums[right]])
        			left = left + 1
        			while left < right and nums[left] == nums[left - 1]:
        				left = left + 1
        return result