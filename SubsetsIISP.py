'''
90. Subsets II
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
        subsets = []
        result = []
        nums = sorted(nums)

        def generate(index, current):
        	if index >= len(nums):
        		subsets.append(current[:])
        		return
        	current.append(nums[index])
        	generate(index + 1, current)
        	current.pop()
        	generate(index + 1, current)

        generate(0, [])
        result.append(subsets[0])

        for index in range(1, len(subsets)):
        	if subsets[index] not in result:
        		result.append(subsets[index])
        return result