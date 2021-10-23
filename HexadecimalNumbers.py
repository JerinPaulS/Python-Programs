'''
Hexadecimal numbers
Problem
You are given a range . You are required to find the number of integers  in the range such that  where  is equal to the sum of digits of  in its hexadecimal (or base 16) representation.

For example,  ( in hexadecimal is written as ). You are aksed  such questions. 

Input format

The first line contains a positive integer  denoting the number of questions that you are asked.
Each of the next  lines contain two integers  and  denoting the range of questions.
Output Format

For each test case, you are required to print exactly  numbers as the output. 

Constraints


Sample Input
3
1 3
5 8
7 12
Sample Output
2
4
6
Time Limit: 2
Memory Limit: 256
Source Limit:
Explanation
For the first test-case, numbers which satisfy the criteria specified are : 2,3. Hence, the answer is 2.

For the second test-case, numbers which satisfy the criteria specified are : 5,6,7 and 8. Hence the answer is 4.

For the third test-case, numbers which satisfy the criteria specified are : 7,8,9,10,11 and 12. Hence the answer is 6.
'''
import math as mt
def hexProb(L,R):
    count = 0
    for i in range(L,R+1):
        sum = 0
        for j in str(hex(i))[2:]:
            sum+=int(j,16)
        if(mt.gcd(i,sum)>1):
            count+=1
    return count
t = int(input()) 
for i in range(t):
    a,b = map(int, input().split())
    print(hexProb(a,b))