'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sum_dict = {}
        result = []
        for left_index in range(0, len(nums) - 1):
        	for right_index in range(left_index + 1, len(nums)):
        		if sum_dict.has_key(nums[left_index] + nums[right_index]):
        			sum_dict[nums[left_index] + nums[right_index]].append((left_index, right_index))
        		else:
        			sum_dict[nums[left_index] + nums[right_index]] = [(left_index, right_index)]

        for left_index in range(0, len(nums) - 1):
        	for right_index in range(left_index + 1, len(nums)):
        		if sum_dict.has_key(target - nums[left_index] - nums[right_index]):
        			temp_list = sum_dict[target - nums[left_index] - nums[right_index]]
        			for s in temp_list:
        				if left_index != right_index and left_index != s[0] and left_index != s[1] and right_index != s[0] and right_index != s[1] and s[0] != s[1]:
        					temp_list = sorted([nums[left_index], nums[right_index], nums[s[0]], nums[s[1]]])
        					if temp_list not in result:
        						result.append(temp_list)

        return result

obj = Solution()
print(obj.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(obj.fourSum([2,2,2,2,2], target = 8))