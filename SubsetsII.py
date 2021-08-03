'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        subsets = []
        list_leng = len(nums)
        
        for mask in range(1 << list_leng):
        	current = []
        	for index in range(list_leng):
        		if (mask & (1 << index)) > 0:
        			current.append(nums[index])
        	subsets.append(current)

        
        subsets = sorted(subsets)
        result = [subsets[0]]
        for index in range(1, len(subsets)):
        	if subsets[index - 1] != subsets[index]:
        		result.append(subsets[index])

        return result
obj = Solution()
print(obj.subsetsWithDup([1,2,3]))    	