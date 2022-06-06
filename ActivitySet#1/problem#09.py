fname = input("Enter file name: ")
fh = open(fname)
lt = list()
for line in fh:
 l = line.split()
 for i in l:
    if i not in lt:
        lt.append(i)
lt.sort()
print(lt) 