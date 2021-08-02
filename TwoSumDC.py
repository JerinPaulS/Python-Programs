'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for index in range(len(nums)):
        	if num_dict.has_key(nums[index]):
        		num_dict[nums[index]].append(index)
        	else:
        		temp = [index]
        		num_dict[nums[index]] = temp

        for val in nums:
        	if num_dict.has_key(target - val):
        		if val == (target - val):
        			if len(num_dict[target - val]) > 1:
        				temp_list = num_dict[val]
        				return [temp_list[0], temp_list[1]]
        		else:
        			return [num_dict[val][0], num_dict[target - val][0]]

obj = Solution()
print(obj.twoSum(nums = [2,7,11,15], target = 9))
print(obj.twoSum(nums = [3,2,4], target = 6))
print(obj.twoSum(nums = [3,3], target = 6))      	