'''
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            pivot, ptr = nums[right], left
            for index in range(left, right):
                if nums[index] <= pivot:
                    nums[ptr], nums[index] = nums[index], nums[ptr]
                    ptr += 1
            nums[ptr], nums[right] = nums[right], nums[ptr]

            if ptr > k:
                return quickSelect(left, ptr - 1)
            elif ptr < k:
                return quickSelect(ptr + 1, right)
            else:
                return nums[ptr]

        return quickSelect(0, len(nums) - 1)