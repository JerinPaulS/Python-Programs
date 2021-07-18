'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        res_str = ""
        if len(nums) == 0:
        	return result
    	res_str = str(nums[0])

        if len(nums) == 1:
        	result.append(res_str)
        	return result
        for index in range(0, len(nums) - 1):
        	if len(res_str) == 0:
        		res_str = str(nums[index])
        	if nums[index + 1] - nums[index] != 1:
        		if res_str == str(nums[index]):
        			result.append(res_str)
        			res_str = ""
        		else:
        			res_str = res_str + "->" + str(nums[index])
        			result.append(res_str)
        			res_str = ""
        if len(res_str) == 0:
        	result.append(str(nums[len(nums) - 1]))
        else:
        	res_str = res_str + "->" + str(nums[len(nums) - 1])
        	result.append(res_str)
        return result

obj = Solution()
#print(obj.summaryRanges([0,1,2,4,5,7]))
#print(obj.summaryRanges([0,2,3,4,6,8,9]))
#print(obj.summaryRanges([-1]))
print(obj.summaryRanges([-1,1,2,3,5,7,8,10,12,13,15]))
#print(obj.summaryRanges([0]))