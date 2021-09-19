'''
673. Number of Longest Increasing Subsequence
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
'''
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        lis = [1] * size
        count = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]: 
                    if lis[j] + 1 == lis[i]:
                        count[i] = count[i] + count[j]
                    if lis[j] + 1 > lis[i]:
                        count[i] = count[j]
                    lis[i] = max(lis[i], lis[j] + 1)
        result = 0
        max_val = max(lis)
        for index in range(size):
            if lis[index] == max_val:
                result = result + count[index]
        return result

obj = Solution()
print(obj.findNumberOfLIS([1,3,5,4,7]))

'''
		j     i
		1 3 5 4 7
	-----------------
lis 	1 2 3 1 1
count	1 1 1 1 1
'''