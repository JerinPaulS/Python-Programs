'''
1736. Latest Time by Replacing Hidden Digits
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"
 

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
'''
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hrs, mins = time.split(":")
        hrs = list(hrs)
        mins = list(mins)
        if hrs[0] == "?":
        	if hrs[1] != "?" and int(hrs[1]) > 3:
        		hrs[0] = "1"
        	else:
        		hrs[0] = "2"
        if hrs[1] == "?":
        	if int(hrs[0]) == 2:
        		hrs[1] = "3"
        	else:
        		hrs[1] = "9"
        if mins[0] == "?":
        	mins[0] = "5"
        if mins[1] == "?":
        	mins[1] = "9"
        return "".join(hrs) + ":" + "".join(mins)