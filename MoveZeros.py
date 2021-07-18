'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr_ptr = 0
        prev_ptr = 0
        while curr_ptr < len(nums):
        	if nums[curr_ptr] == 0:
        		curr_ptr = curr_ptr + 1
        	else:
        		temp = nums[curr_ptr]
        		nums[curr_ptr] = nums[prev_ptr]
        		nums[prev_ptr] = temp
        		curr_ptr = curr_ptr + 1
        		prev_ptr = prev_ptr + 1
        return nums