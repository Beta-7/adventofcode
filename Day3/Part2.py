import time
import re
import numpy as np
start = time.time()
inputs = []
grid = [['0x0' for i in range(1000)] for j in range(1000)]

ans = 0
claims = {}
for a in range(1,1397):
    claims[a] = '1'
with open('input.txt') as my_file:
    for line in my_file:

        #1350 @ 975,74: 23x16
        nums = re.findall(r'\d+', line)
        # nums[0] = index, nums[1] = X, nums[2] = Y, nums[3] = Xsize, nums[4] = Ysize
        for x in range(int(nums[1]),int(nums[1])+int(nums[3])):
            for y in range(int(nums[2]),int(nums[2])+int(nums[4])):
                if grid[x][y]!='0x0':
                    claims[int(nums[0])]='0'
                    claims[int(grid[x][y])]='0'
                    #print(nums[0])
                    #print(grid[x][y])
                    grid[x][y]=nums[0]
                if grid[x][y]=='0x0':
                    grid[x][y]=nums[0]

for a in range(1,1397):
    if claims[a] == '1':
        print('The only non-overlaping claim is #{0}, it took me {1:.2f}s to find it'.format(a,time.time()-start))
        break
