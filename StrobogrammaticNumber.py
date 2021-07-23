'''
246. Strobogrammatic Number
A strobogrammatic number is a nuumber that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is stobogrammatic. The number is represented as a string.

Example 1:

Input: "69"
Output: true

Example 1:

Input: "88"
Output: true

Example 1:

Input: "962"
Output: false
'''
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: boolean
        """
        start = 0
        end = len(num) - 1
        while start <= end:
        	if num[start] == num[end]:
        		if num[start] not in "018":
        			return False
        	else:
        		if num[start] == "6" and num[end] == "6":
        			return False
        		if num[start] == "9" and num[end] == "9":
        			return False
        	start = start + 1
        	end = end - 1
        return True

obj = Solution()
print("True", obj.isStrobogrammatic("69"))
print("True", obj.isStrobogrammatic("88"))
print("False", obj.isStrobogrammatic("962"))
print("False", obj.isStrobogrammatic("111191111"))
print("False", obj.isStrobogrammatic("111161111"))
print("True", obj.isStrobogrammatic("111181111"))
print("False", obj.isStrobogrammatic("111121111"))
print("True", obj.isStrobogrammatic("111101111"))
print("True", obj.isStrobogrammatic("1908061"))