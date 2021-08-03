'''
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        current = []
        
        def generateSubsets(index):
            subsets.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                generateSubsets(i + 1)
                current.pop()
                
        generateSubsets(0)
                
        return subsets

'''
		def genetateSubsets(index):
			if index >= len(nums):
				substes.append(current.copy())
				return
			current.append(nums[index])
			generateSubstes(index + 1)
			current.pop()
			generateSubsets(index + 1)
'''
'''
		for mask in range(1 << len(nums)):
			current = []
			for index in range(len(nums)):
				if (mask & 1 << index) > 0:
					current.append(nums[index])
			subset.append(current)
'''