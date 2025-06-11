#!/usr/bin/env python3

#Author: Andrew Holder
#Author ID: 146631213
#Date Created: 2025/05/28

import sys


if len(sys.argv) == 1:
    timer = 3

elif len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
    

