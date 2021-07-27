'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n = n - 1
            if n <= 0:
                return True
            else:
                return False
            
        for index in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n = n - 1
            if flowerbed[index] == 0:
                if index - 1 > 0 and index + 1 < len(flowerbed) - 1 and flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n = n - 1
                if index - 1 > 0 and index + 1 > len(flowerbed) - 1 and flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
                    n = n - 1

        if n <= 0:
            return True
        else:
            return False
obj = Solution()
print(obj.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(obj.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))