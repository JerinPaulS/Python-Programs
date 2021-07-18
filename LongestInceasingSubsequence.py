'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        temp = []
        temp.append(nums[0])
        row = 0
        col = 0
        for i in range(1, len(nums)):
            if temp[col] >= nums[i]:
                temp.append(nums[i])
                col = col + 1
            else:
                result.append(temp)
                temp = []
                temp.append(nums[i])
                row = row + 1
                col = 0
        result.append(temp)
        print result
        return len(result)
        

obj = Solution()
print(obj.lengthOfLIS([4,10,4,3,8,9]))
#print(obj.lengthOfLIS([0,1,0,3,2,3]))
#print(obj.lengthOfLIS([7,7,7,7,7,7,7]))

'''
result = [1] * len(nums)
        for index in range(len(nums) -1, -1, -1):
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i]:
                    result[index] = max(result[index], 1 + result[i])
        return max(result)
'''