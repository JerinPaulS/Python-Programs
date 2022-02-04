'''
525. Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_dict = collections.defaultdict(int)
        curr_sum = 0
        result = 0
        
        for index, num in enumerate(nums):
            if num == 0:
                num = -1
            curr_sum += num
            if curr_sum == 0:
                result = max(result, index + 1)
                continue
            if curr_sum in sum_dict:
                result = max(result, index - sum_dict[curr_sum])
            else:
                sum_dict[curr_sum] = index
        return result