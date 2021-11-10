'''
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

Example
 

There are  and  at indices  and . Return .

Function Description

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

int arr[n]: an array of integers
int r: the common ratio
Returns

int: the number of triplets
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

Constraints

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and 

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .
'''
import math
import os
import random
import re
import sys
import collections
# Complete the countTriplets function below.

def countTriplets(arr, r):
	num_freq = collections.defaultdict(list)
	max_val = max(arr)
	expected = [1]
	val = r
	expected.append(val)
	while val <= max_val:		
		val *= r
		expected.append(val)
	for index, num in enumerate(arr):
		if num in expected:
			num_freq[num].append(index)

	keys = num_freq.keys()
	result = 0
	keys.sort()
	print keys, num_freq
	for index, key in enumerate(keys):
		if index == 0 or index == len(keys) - 1:
			continue
		if (key // r) in num_freq and (key * r) in num_freq:
			result += len(num_freq[key // r]) * len(num_freq[key]) * len(num_freq[key * r])

	return result

print(countTriplets([1, 5, 5, 25, 125], 5))


'''
	v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return count
'''