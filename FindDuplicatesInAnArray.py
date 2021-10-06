'''
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for index in range(len(nums)):
        	if nums[abs(nums[index]) - 1] < 0:
        		result.append(abs(nums[index]))
        	else:
        		nums[abs(nums[index]) - 1] = -1 * nums[abs(nums[index]) - 1]
        return result

obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))