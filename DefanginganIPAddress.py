'''
1108. Defanging an IP Address
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #address = address.replace(".", "[.]")
        index = 0
        while index < len(address):
        	if address[index] == ".":
        		address = address[:index] + "[.]" + address[index + 1:]
        		index = index + 2
        	index = index + 1
        return "".join(address)