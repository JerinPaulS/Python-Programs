'''
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_freq = {}
        init_index = {}
        max_degree = 0
        result = 0
        for index in range(len(nums)):
        	temp = 0
        	if init_index.has_key(nums[index]) == False:
        		init_index[nums[index]] = index
        	if digit_freq.has_key(nums[index]):
        		digit_freq[nums[index]] = digit_freq[nums[index]] + 1
        		temp = digit_freq[nums[index]]
        	else:
        		digit_freq[nums[index]] = 1
        		temp = 1
        	if temp > max_degree:
        		max_degree = temp
        		result = index - init_index[nums[index]] + 1
        	elif temp == max_degree:
        		result = min(result, index - init_index[nums[index]] + 1)
        return result

obj = Solution()
print(obj.findShortestSubArray([2,1,1,2,1,3,3,3,1,3,1,3,2]))