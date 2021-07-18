'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
        	a = ("0" * (len(b) - len(a))) + a
        elif len(a) > len(b):
        	b = ("0" * (len(a) - len(b))) + b

        carry = "0"
        res = ""
        for i in reversed(range(len(a))):
        	if a[i] == b[i] and a[i] == "0":
        		res = carry + res
        		carry = "0"
        	if a[i] == b[i] and a[i] == "1":
        		if carry == "1":
        			res = carry + res
        		else:
        			carry = "1"
        			res = "0" + res
        	if a[i] != b[i]:
        		if carry == "1":
        			res = "0" + res
        		else:
        			res = "1" + res
        if "1" not in (carry + res):
        	return("0")
        if carry == "1":
        	return(carry + res)
        else:
        	return(res)


obj = Solution()
print(obj.addBinary(a = "11", b = "1"))
print(obj.addBinary(a = "11", b = "11"))
print(obj.addBinary(a = "1010", b = "1011"))