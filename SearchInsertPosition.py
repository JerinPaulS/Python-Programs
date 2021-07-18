'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        start = 0
        last = len(nums) - 1
        while(start <= last):
        	mid = int((start + last) / 2)
        	if target < nums[mid]:
        		last = mid - 1
        	elif target > nums[mid]:
        		start = mid + 1
        	else:
        		return(mid)
        if len(nums) == 1:
            if target < nums[0]:
                return(0)
            else:
                return(1)
        if target < nums[mid]:
            return(mid)
        else:
            return(mid + 1)

obj = Solution()
#print(obj.searchInsert([1,3,5,6],5))
#print(obj.searchInsert([1,3,5,6],2))
#print(obj.searchInsert([1,3,5,6],7))
#print(obj.searchInsert([1,3,5,6],0))
print(obj.searchInsert([1],0))