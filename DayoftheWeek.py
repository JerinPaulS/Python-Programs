'''
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        countDays = 0
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(1971, year):
            if self.leap_year(i):
                countDays = countDays + 366
            else:
                countDays = countDays + 365

        for i in range(month - 1):
            countDays += monthDays[i]

        if month > 2 and self.leap_year(year):
            countDays = countDays + 1

        countDays = countDays + day - 1
        return week[(countDays + 4) % 7]

    def leap_year(self, year):
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        return False

obj = Solution()
print(obj.dayOfTheWeek(day = 31, month = 8, year = 2019))        