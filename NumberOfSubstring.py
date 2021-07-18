'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2'''
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if(string[i] == sub_string[0]):
            j = 0
            temp = 0
            for k in range(len(sub_string)):
                if((i + j) < len(string) and temp == 0):
                    if(string[i + j] == sub_string[k]):
                        j = j + 1
                    else:
                        temp = 1
                        break
            if(temp == 0 and j == len(sub_string)):
                count = count + 1

    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
