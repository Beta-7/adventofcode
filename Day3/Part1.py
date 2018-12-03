import time
import re
import numpy as np
start = time.time()
inputs = []
grid = [['0' for i in range(8)] for j in range(8)]
#for a in range(0,800):
#    for b in range(0,800):
#        grid.append(0)
ans = 0
with open('input.txt') as my_file:
    for line in my_file:

        #1350 @ 975,74: 23x16
        nums = re.findall(r'\d+', line)
        # nums[0] = index, nums[1] = X, nums[2] = Y, nums[3] = Xsize, nums[4] = Ysize
        for x in range(int(nums[1]),int(nums[1])+int(nums[3])):
            for y in range(int(nums[2]),int(nums[2])+int(nums[4])):
                grid[x][y]=str(int(grid[x][y])+1)
                if int(grid[x][y]) >= 2:
                ans+=1

print(ans)
