'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n/2 times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = nums[0]
        count = 0
        for val in nums:
        	if count == 0:
        		element = val
        		count = 1
        	elif element == val:
        		count = count + 1
        	else:
        		count = count - 1
        return element

obj = Solution()
print(obj.majorityElement([3,2,3]))
print(obj.majorityElement([2,2,1,1,1,2,2]))
print(obj.majorityElement([3]))