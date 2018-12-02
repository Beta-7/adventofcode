import time
filepath = 'input.txt'
zbir = 0
starttime=time.time()
frequencies = list()
frequencies.append(0)
set = {0}
def duplicates(checkAgainst):
    if checkAgainst in set:
        return checkAgainst
    set.add(checkAgainst)

while True:
    with open(filepath) as fp:
       line = fp.readline()
       while line:
           zbir = zbir + int(line)
           frequencies.append(zbir)
           line = fp.readline()
           start=time.time()
           dupes = duplicates(zbir)
           # print('It took {0:0.1f} seconds'.format(time.time() - start))
           if dupes!=None:
               print(dupes)
               print('It took {0:0.1f} seconds'.format(time.time() - start))
               print('It took {0:0.1f} total'.format(time.time() - starttime))
               quit()
