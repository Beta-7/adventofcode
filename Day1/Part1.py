filepath="input.txt"
zbir =0
with open(filepath) as fp:
   line = fp.readline()
   while line:
       zbir = zbir + int(line)
       line = fp.readline()
print(zbir)
