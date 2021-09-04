'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		left = self.binsearch(nums, target, True)
		right = self.binsearch(nums, target, False)
		return [left, right]

	def binsearch(self, nums, target, direction):
		start = 0
		end = len(nums) - 1
		index = -1		
		while start <= end:
			mid = (start + end) // 2
			if nums[mid] < target:
				start = mid + 1
			elif nums[mid] > target:
				end = mid - 1
			else:
				index = mid
				if direction:
					end = mid - 1
				else:
					start = mid + 1

		return index