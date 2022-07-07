#tuples_ex10.2
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = {}
for line in handle:
    if "From:" in line: continue
    elif "From" in line:
        tmp = line.split( )
        tmp = str(tmp[5]).split(":")
        if tmp[0] not in hours:
            hours[tmp[0]] = 1
        else: hours[tmp[0]]=hours.get(tmp[0],0) + 1
    else: continue
for k,v in sorted(hours.items()):
    print(k,v)