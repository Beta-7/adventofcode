def checkLetters(str,str2):
    cnt=0
    if str==str2:
        return False
    for a in range(0,len(str)):
        if cnt == 2:
            return False
        if str[a] != str2[a]:
            cnt +=1
    return True
inputs = []
with open('input.txt') as my_file:
    for line in my_file:
        inputs.append(line)


for a in range(0, len(inputs)):
    for b in range(a, len(inputs)):
        if checkLetters(inputs[a],inputs[b]):
            print('Checking {0} and {1}'.format(inputs[a],inputs[b]))
