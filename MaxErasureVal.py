'''
Maximum Erasure Value
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
'''
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set()
        start = 0
        end = 0
        temp_sum = 0
        max_sum = 0
        flag = 0
        while start < len(nums) and end != len(nums):
        	if flag == 1:
        		break
        	while end < len(nums) and start <= end:
        		if nums[end] in elements:
        			elements.remove(nums[start])
        			temp_sum = temp_sum - nums[start]
        			start = start + 1
        			break
        		else:
        			elements.add(nums[end])
        			temp_sum = temp_sum + nums[end]
        			end = end + 1
        		print(elements)
        		if temp_sum > max_sum:
        			max_sum = temp_sum
        		if end == len(nums):
        			flag = 1
        			break

        print(max_sum)


obj = Solution()
obj.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434])
obj.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])
obj.maximumUniqueSubarray([4,2,4,5,6])
obj.maximumUniqueSubarray([10000,1,10000,1,1,1,1,1,1])