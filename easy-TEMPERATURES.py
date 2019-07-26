https://www.codingame.com/ide/puzzle/temperatures

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
a=5527
b=0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if abs(t)<a:
        a=abs(t)
        b=t
    elif abs(t)==a:
        b=max(b,t)
    
        
print(b)

