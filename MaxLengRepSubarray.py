'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return 0
        col_len = len(nums1)
        row_len = len(nums2)
        result = []
        for row in range(row_len + 1):
            temp = []
            for col in range(col_len + 1):
                temp.append(0)
            result.append(temp)
        for row in range(1, (row_len + 1)):
            for col in range(1, (col_len + 1)):
                if nums1[col - 1] == nums2[row - 1]:
                    result[row][col] = 1 + result[row - 1][col - 1]
        res_max = 0
        for row in range(1, (row_len) + 1):
            if res_max < max(result[row]):
                res_max = max(result[row])
        return res_max

obj = Solution()
#print(obj.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(obj.findLength([0,1,1,1,1],[1,0,1,0,1]))
#print(obj.findLength([5,14,53,80,48],[50,47,3,80,83]))

'''
		0, 1, 1, 1, 1
	[0, 1, 2, 3, 4, 5], 
1	[0, 1, 2, 3, 4, 5], 
0	[0, 1, 2, 3, 4, 5], 
1	[0, 1, 2, 3, 4, 5], 
0	[0, 1, 2, 3, 4, 5], 
1	[0, 1, 2, 3, 4, 5]


'''