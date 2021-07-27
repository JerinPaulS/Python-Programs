'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums = sorted(nums)

        for index in range(len(nums) - 2):
            start = index + 1
            end = len(nums) - 1
            while start < end:
                temp_sum = nums[index] + nums[start] + nums[end]
                if temp_sum > target:
                    end = end - 1
                else:
                    start = start + 1
                if abs(target - temp_sum) < abs(target - result):
                    result = temp_sum

        return result