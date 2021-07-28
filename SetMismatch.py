'''
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        result = []
        for index in range(len(nums) - 1):
        	xor_res = nums[index + 1] ^ nums[index]
        	if xor_res == 0:
        		result.append(nums[index])
        		break
        for val in range(1, len(nums) + 1):
        	if val not in nums:
        		result.append(val)
        return result

obj = Solution()
print(obj.findErrorNums([1,2,2,4]))