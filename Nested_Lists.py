"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N , the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""


if __name__ == '__main__':

    val_min = 100000
    temp = 1000
    name_list = []
    score_list = []
    second_last = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_list.append(name)
        score_list.append(score)
        name_list.append(score_list)
        score_list = []

        if val_min > score:
            val_min = score        

    for nm in name_list:
        if nm[1] < temp and nm[1] != val_min:
            temp = nm[1]

    for nm in name_list:
        if nm[1] == temp:
            second_last.append(nm[0])

    second_last.sort()
    for nm in second_last:
        print(nm)
