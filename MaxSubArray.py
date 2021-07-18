'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = nums[0]
        global_max = nums[0]
        for index in range(1, len(nums)):
        	local_max = max(local_max + nums[index], nums[index])
        	if global_max < local_max:
        		global_max = local_max

        return(global_max)

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray([5,4,-1,7,8]))