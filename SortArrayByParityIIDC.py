'''
Sort Array By Parity II
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 

Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000
 

Follow Up: Could you solve it in-place?
'''
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr = 1
        prev = 0

        while curr < len(nums) and prev < len(nums):
        	if nums[prev] % 2 != 0 and nums[curr] %2 == 0:
        		nums[prev], nums[curr] = nums[curr], nums[prev]
        		prev = prev + 2
        		curr = curr+ 2
        	else:
        		if nums[prev] % 2 == 0:
        			prev = prev + 2
        		if nums[curr] % 2 != 0:
        			curr = curr + 2
        return nums