https://www.codingame.com/ide/puzzle/the-descent

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    a = 0
    b = 0
    for i in range(8):
        height = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if height > a:
            a = height
            b = i

    print(b)
