https://www.codingame.com/ide/puzzle/ascii-art

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
row = [input() for i in range(h)]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# searching list
letter_list = []

# target output list
target_list = []

# format the searching list and initial the target output list
for i in range(h):
    line = row[i]
    start = 0
    row_list = []
    while start < l * 27:
        row_letter = line[start:start+l]
        start += l
        row_list.append(row_letter)
    letter_list.append(row_list)
    target_list.append([])

# start to search one by one and append to target list
begin = ord('A')
for target_letter in t:
    pos = ord(target_letter.upper()) - begin
    if pos > 25 or pos < 0:
        pos = 26
    for row_num in range(h):
        target_list[row_num].append(letter_list[row_num][pos])

# print the target output list
for i in range(h):
    print("".join(target_list[i]))
