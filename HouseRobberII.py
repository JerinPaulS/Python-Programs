'''
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
        	return 0
        if size <= 3:
        	return max(nums)

        def findmax(houses):
        	leng = len(houses)
        	if leng == 0:
        		return 0
        	if leng <= 2:
        		return max(houses)

        	dp = [0] * leng
        	dp[0] = houses[0]
        	dp[1] = max(houses[0], houses[1])

        	for index in range(2, leng):
        		dp[index] = max((dp[index - 2] + houses[index]), dp[index - 1])

        	return dp[leng - 1]

        max1 = findmax(nums[1:size])
        max2 = findmax(nums[0:size - 1])

        return max(max1, max2)