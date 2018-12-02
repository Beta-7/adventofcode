import collections

filepath="input.txt"

bukvi3=0
bukvi2=0
with open(filepath) as fp:
   line = fp.readline()
   while line:
       cnt =collections.defaultdict(int)
       for character in line:
           cnt[character] += 1
       line = fp.readline()
       if 2 in cnt.values():
           bukvi2+=1

       if 3 in cnt.values():
           bukvi3+=1

print(bukvi3*bukvi2)
