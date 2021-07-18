'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == 1:
        	return False
        res_dict = {}
        for val in nums:
        	if res_dict.has_key(val):
        		return True
        	else:
        		res_dict[val] = 1

        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
print(obj.containsDuplicate([1,2,3,4]))
print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

'''

nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

'''