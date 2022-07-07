#lists_ex8.5
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if "From:" in line: continue
    elif "From" in line:
        lst = line.split("From")
        new_lst = str(lst[1]).split( )
        print(new_lst[0])
        count = count+1
    else: continue
print("There were", count, "lines in the file with From as the first word")