'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 106
It is guaranteed there is at least one way to partition nums as described.
'''
class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_left = [nums[0]]
        for index in range(1, len(nums)):
            max_left.append(max(max_left[-1], nums[index]))
        
        min_right = [nums[-1]]
        for index in range(len(nums) - 2, -1, -1):
            min_right.append(min(min_right[-1], nums[index]))
            
        min_right = min_right[::-1]
        
        for index in range(1, len(nums)):
            if max_left[index - 1] <= min_right[index]:
				return index

obj = Solution()
print(obj.partitionDisjoint([5,0,3,8,6]))
print(obj.partitionDisjoint([1,1,1,0,6,12]))
print(obj.partitionDisjoint([90,47,69,10,43,92,31,73,61,97]))
'''
for index in range(1, len(nums)):
            left = nums[:index]
            right = nums[index:]
            if max(left) <= min(right):
                return index
'''