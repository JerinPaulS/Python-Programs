'''
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        size = len(nums)
        if size == 1:
        	return False
        if total % 2 != 0:
        	return False
        dp = {}
        target = total // 2
        def helper(index, target):
        	if target == 0:
        		return True
        	if target < 0 or index >= size:
        		return False
        	if (index, target) not in dp:
        		dp[(index, target)] = helper(index + 1, target - nums[index]) or helper(index + 1, target)
        	return dp[(index, target)]

        return helper(0, target)