'''
41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
        	if nums[index] < 0:
        		nums[index] = 0

        for index in range(len(nums)):
        	val = abs(nums[index])
        	if val - 1 >=0 and val - 1 < len(nums):
        		if nums[val - 1] > 0:
        			nums[val - 1] = -nums[val - 1]
        		elif nums[val - 1] == 0:
        			nums[val - 1] = -1 * (len(nums) + 1)

        for index in range(1, len(nums) + 1):
        	if nums[index - 1] >= 0:
        		return index
        return len(nums) + 1